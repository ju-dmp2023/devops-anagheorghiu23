from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calculation import Calculation
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.result_response import ResultResponse
from ...types import Response


def _get_kwargs(
    *,
    body: Calculation,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/calculate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, HTTPValidationError, ResultResponse]]:
    if response.status_code == 200:
        response_200 = ResultResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, HTTPValidationError, ResultResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Calculation,
) -> Response[Union[ErrorResponse, HTTPValidationError, ResultResponse]]:
    """Basic arithmetic calculation

     Perform a basic arithmetic calculation.

    Args:
        body (Calculation): The request body containing operands and operation.

    Returns:
        ResultResponse: The result of the calculation.

    Raises:
        HTTPException: 500 if the calculation fails.

    Args:
        body (Calculation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, HTTPValidationError, ResultResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Calculation,
) -> Optional[Union[ErrorResponse, HTTPValidationError, ResultResponse]]:
    """Basic arithmetic calculation

     Perform a basic arithmetic calculation.

    Args:
        body (Calculation): The request body containing operands and operation.

    Returns:
        ResultResponse: The result of the calculation.

    Raises:
        HTTPException: 500 if the calculation fails.

    Args:
        body (Calculation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, HTTPValidationError, ResultResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Calculation,
) -> Response[Union[ErrorResponse, HTTPValidationError, ResultResponse]]:
    """Basic arithmetic calculation

     Perform a basic arithmetic calculation.

    Args:
        body (Calculation): The request body containing operands and operation.

    Returns:
        ResultResponse: The result of the calculation.

    Raises:
        HTTPException: 500 if the calculation fails.

    Args:
        body (Calculation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, HTTPValidationError, ResultResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Calculation,
) -> Optional[Union[ErrorResponse, HTTPValidationError, ResultResponse]]:
    """Basic arithmetic calculation

     Perform a basic arithmetic calculation.

    Args:
        body (Calculation): The request body containing operands and operation.

    Returns:
        ResultResponse: The result of the calculation.

    Raises:
        HTTPException: 500 if the calculation fails.

    Args:
        body (Calculation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, HTTPValidationError, ResultResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
