"""Dependencies shared by all API v1 routers (movies, books)"""

from typing import Annotated

from fastapi import Header, HTTPException, Request, status

from core.config import API_TOKENS

UNSAFE_METHODS = frozenset({"POST", "PUT", "PATCH", "DELETE"})

responses_401 = {
    status.HTTP_401_UNAUTHORIZED: {
        "description": "Unauthorized: API token is missing or invalid",
        "content": {
            "application/json": {
                "example": {"detail": "Invalid API token"}
            }
        },
    }
}


def api_token_required(
        request: Request,
        api_token: Annotated[
            str | None,
            Header(
                alias="x-auth-token",
                description="API token (required for unsafe methods)",
            ),
        ] = None,
) -> None:
    """Check the API token from the header for unsafe methods"""
    if request.method not in UNSAFE_METHODS:
        return

    if api_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API token is required",
        )

    if api_token not in API_TOKENS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API token",
        )
