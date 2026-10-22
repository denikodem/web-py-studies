"""Application configuration"""

# Tokens were generated once with the `secrets` module:
#   import secrets; secrets.token_urlsafe(16)
# They are fixed here on purpose: if we generated them at import time,
# they would change on every restart/reload and we could not use them.
API_TOKENS = frozenset(
    {
        "5iWXKmR8DrKg6GNrYbNrFg",
        "QHJqnS0WUjtTfPXCcSfNYw",
        "HrV2VJcPxVgDuz7B_7wrfg",
    }
)
