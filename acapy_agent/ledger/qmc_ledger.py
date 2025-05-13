"""QMC ledger implementation."""

import asyncio
import hashlib
import json
import logging
import os
import os.path
import tempfile
from datetime import date, datetime, timezone
from io import StringIO
from pathlib import Path
from time import time
from typing import List, Optional, Tuple, Union

from indy_vdr import Pool, Request, VdrError, ledger, open_pool

from ..cache.base import BaseCache
from ..core.profile import Profile
from ..messaging.valid import IndyDID
from ..storage.base import BaseStorage, StorageRecord
from ..utils import sentinel
from ..utils.env import storage_path
from ..wallet.base import BaseWallet, DIDInfo
from ..wallet.did_posture import DIDPosture
from ..wallet.error import WalletNotFoundError
from .base import BaseLedger, Role
from .endpoint_type import EndpointType
from .error import (
    BadLedgerRequestError,
    ClosedPoolError,
    LedgerConfigError,
    LedgerError,
    LedgerTransactionError,
)
from .util import TAA_ACCEPTED_RECORD_TYPE

class QmcLedger(BaseLedger):
    """QMC ledger class."""

    BACKEND_NAME = "qmc"

    def __init__(
        self,
        url,
        profile: Profile,
    ):
        """Initialize an IndyVdrLedger instance.

        Args:
            pool: The pool instance handling the raw ledger connection
            profile: The active profile instance
        """
        # print("__init__ QmcLedger")
        
        self.url = url
        self.profile = profile 

    async def _create_credential_definition_request(
        self,
        public_info: DIDInfo,
        credential_definition_json: str,
        write_ledger: bool = True,
        endorser_did: Optional[str] = None,
    ):
        print("_create_credential_definition_request")

    async def _create_revoc_reg_def_request(
        self,
        public_info: DIDInfo,
        revoc_reg_def_json: str,
        write_ledger: bool = True,
        endorser_did: Optional[str] = None,
    ):
        print("_create_revoc_reg_def_request")
    
    async def _create_schema_request(
        self,
        public_info: DIDInfo,
        schema_json: str,
        write_ledger: bool = True,
        endorser_did: Optional[str] = None,
    ):
        print("_create_schema_request")

    async def accept_txn_author_agreement(
        self, taa_record: dict, mechanism: str, accept_time: Optional[int] = None
    ):
        print("accept_txn_author_agreement")

    async def fetch_schema_by_id(self, schema_id: str) -> dict:
        print("fetch_schema_by_id")
        schema_data = {
            "ver": "1.0",
            "id": schema_id,
            "name": "schema_name",
            "version": "schema_version",
            "attrNames": "",
            "seqNo": "",
        }
        return schema_data 
    
    async def fetch_schema_by_seq_no(self, seq_no: int) -> dict:
        print("fetch_schema_by_seq_no")
        schema_data = {
            "ver": "1.0",
            "id": "schema_id",
            "name": "schema_name",
            "version": "schema_version",
            "attrNames": "",
            "seqNo": "",
        }
        return schema_data
    
    async def get_txn_author_agreement(self, reload: bool = False) -> dict:
        """Get the current transaction author agreement, fetching it if necessary."""
        print("get_txn_author_agreement")
        d = {}
        return d
    
    async def get_all_endpoints_for_did(self, did: str) -> dict:
        print("get_all_endpoints_for_did")
        d = {}
        return d
    
    async def get_credential_definition(self, credential_definition_id: str) -> dict:
        print("get_credential_definition")
        d = {}
        return d
    
    async def get_endpoint_for_did(
        self, did: str, endpoint_type: Optional[EndpointType] = None
    ) -> str:
        print("get_endpoint_for_did")
        return ""
    
    async def get_key_for_did(self, did: str) -> Optional[str]:
        print("get_key_for_did")
        return ""
    
    async def get_latest_txn_author_acceptance(self) -> dict:
        print("get_latest_txn_author_acceptance")
        return {}
    
    async def get_nym_role(self, did: str) -> Role:
        print("get_nym_role")
        return Role.ENDORSER

    async def get_revoc_reg_def(self, revoc_reg_id: str) -> dict:
        print("get_revoc_reg_def")
        return {}
    
    async def get_revoc_reg_delta(
        self, revoc_reg_id: str, timestamp_from=0, timestamp_to=None
    ) -> Tuple[dict, int]:
        print("get_revoc_reg_delta")
        return ({}, 1)
    
    async def get_revoc_reg_entry(
        self, revoc_reg_id: str, timestamp: int
    ) -> Tuple[dict, int]:
        print("get_revoc_reg_entry")
        return ({}, 1)
    
    async def get_schema(self, schema_id: str) -> dict:
        print("get_schema")
        return {}
    
    async def get_txn_author_agreement(self, reload: bool = False) -> dict:
        print("get_txn_author_agreement")
        return {}
    
    async def get_wallet_public_did(self) -> DIDInfo:
        """Fetch the public DID from the wallet."""
        async with self.profile.session() as session:
            wallet = session.inject(BaseWallet)
            return await wallet.get_public_did()
        
    async def is_ledger_read_only(self) -> bool:
        print("is_ledger_read_only")
        return False
    
    def nym_to_did(self, nym: str) -> str:
        print("nym_to_did")
        return ""
    
    def read_only(self) -> bool:
        print("read_only")
        return False
    
    async def register_nym(
        self,
        did: str,
        verkey: str,
        alias: Optional[str] = None,
        role: Optional[str] = None,
        write_ledger: bool = True,
        endorser_did: Optional[str] = None,
    ) -> Tuple[bool, dict]:
        print("register_nym")
        return (True, {})
    
    async def rotate_public_did_keypair(self, next_seed: Optional[str] = None) -> None:
        print("rotate_public_did_keypair")

    async def send_revoc_reg_def(
        self,
        revoc_reg_def: dict,
        issuer_did: Optional[str] = None,
        write_ledger: bool = True,
        endorser_did: Optional[str] = None,
    ) -> dict:
        print("rotate_public_did_keypair")
        return {}
    
    async def send_revoc_reg_entry(
        self,
        revoc_reg_id: str,
        revoc_def_type: str,
        revoc_reg_entry: dict,
        issuer_did: Optional[str] = None,
        write_ledger: bool = True,
        endorser_did: Optional[str] = None,
    ) -> dict:
        print("send_revoc_reg_entry")
        return {}
    
    async def txn_endorse(
        self,
        request_json: str,
        endorse_did: Optional[DIDInfo] = None,
    ) -> str:
        print("txn_endorse")
        return ""
    
    async def txn_submit(
        self,
        request_json: str,
        sign: bool,
        taa_accept: Optional[bool] = None,
        sign_did: DIDInfo = sentinel,
        write_ledger: bool = True,
    ) -> str:
        print("txn_submit")
        return ""
    
    async def update_endpoint_for_did(
        self,
        did: str,
        endpoint: str,
        endpoint_type: Optional[EndpointType] = None,
        write_ledger: bool = True,
        endorser_did: Optional[str] = None,
        routing_keys: Optional[List[str]] = None,
    ) -> bool:
        print("update_endpoint_for_did")
        return True
    
    async def fetch_txn_author_agreement(self) -> dict:
        print("fetch_txn_author_agreement")
        return {}