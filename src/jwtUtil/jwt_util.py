import logging

import jwt
from fastapi import HTTPException
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from src.core.config import settings
import py_eureka_client.eureka_client as eureka_client
import asyncio

auth_setting = settings.auth_settings

logger = logging.getLogger("uvicorn.error")


class JWTUtil:
    public_key = "key"

    @classmethod
    def get_claims(cls, token: str) -> dict:
        token = token.replace("Bearer ", "")
        try:
            claims = jwt.decode(
                token,
                key=cls.public_key,
                algorithms=[
                    "RS256",
                ],
                options={"verify_exp": True},
            )
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
        except jwt.InvalidSignatureError:
            raise HTTPException(status_code=401, detail="Invalid signature")
        if claims["tokenType"] == "ACCESS":
            return claims
        else:
            raise HTTPException(status_code=401, detail="Invalid tokenType claim")

    @classmethod
    async def load_keys(cls, interval: int):
        while True:
            ans = await eureka_client.do_service_async(
                settings.auth_settings.domain_name,
                "/api/auth/jwt/publicKey",
                return_type="string",
            )
            ans = (
                "-----BEGIN PUBLIC KEY-----\n"
                + "\n".join(ans[i : i + 64] for i in range(0, len(ans), 64))
                + "\n-----END PUBLIC KEY-----"
            ).encode()

            cls.public_key = load_pem_public_key(ans)

            logger.info(
                f"Getting new public key from: {settings.auth_settings.domain_name}"
            )

            await asyncio.sleep(interval)
