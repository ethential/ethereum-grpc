# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethereum.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ethereum.proto',
  package='protoeth',
  syntax='proto3',
  serialized_options=b'Z\010protoeth',
  serialized_pb=b'\n\x0e\x65thereum.proto\x12\x08protoeth\"\x10\n\x0eGetAccountsReq\"#\n\x0fGetAccountsResp\x12\x10\n\x08\x61\x63\x63ounts\x18\x01 \x03(\t\" \n\rGetBalanceReq\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"!\n\x0eGetBalanceResp\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\t\"\x18\n\x06TxHash\x12\x0e\n\x06txhash\x18\x01 \x01(\t\"&\n\x0fTransactionInfo\x12\x13\n\x0btransaction\x18\x01 \x01(\t\"\x1e\n\tTxReceipt\x12\x11\n\ttxReceipt\x18\x01 \x01(\t\"\x1a\n\x0cRawTxRequest\x12\n\n\x02tx\x18\x01 \x01(\t\"\x1c\n\nTxResponse\x12\x0e\n\x06txData\x18\x01 \x01(\t2\xe6\x02\n\x0fProtoEthService\x12\x44\n\x0bGetAccounts\x12\x18.protoeth.GetAccountsReq\x1a\x19.protoeth.GetAccountsResp\"\x00\x12\x41\n\nGetBalance\x12\x17.protoeth.GetBalanceReq\x1a\x18.protoeth.GetBalanceResp\"\x00\x12?\n\x0eGetTransaction\x12\x10.protoeth.TxHash\x1a\x19.protoeth.TransactionInfo\"\x00\x12G\n\x13SendRawTransactions\x12\x16.protoeth.RawTxRequest\x1a\x14.protoeth.TxResponse\"\x00\x30\x01\x12@\n\x15GetTransactionReceipt\x12\x10.protoeth.TxHash\x1a\x13.protoeth.TxReceipt\"\x00\x42\nZ\x08protoethb\x06proto3'
)




_GETACCOUNTSREQ = _descriptor.Descriptor(
  name='GetAccountsReq',
  full_name='protoeth.GetAccountsReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=44,
)


_GETACCOUNTSRESP = _descriptor.Descriptor(
  name='GetAccountsResp',
  full_name='protoeth.GetAccountsResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accounts', full_name='protoeth.GetAccountsResp.accounts', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=81,
)


_GETBALANCEREQ = _descriptor.Descriptor(
  name='GetBalanceReq',
  full_name='protoeth.GetBalanceReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='protoeth.GetBalanceReq.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=115,
)


_GETBALANCERESP = _descriptor.Descriptor(
  name='GetBalanceResp',
  full_name='protoeth.GetBalanceResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='balance', full_name='protoeth.GetBalanceResp.balance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=150,
)


_TXHASH = _descriptor.Descriptor(
  name='TxHash',
  full_name='protoeth.TxHash',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txhash', full_name='protoeth.TxHash.txhash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=176,
)


_TRANSACTIONINFO = _descriptor.Descriptor(
  name='TransactionInfo',
  full_name='protoeth.TransactionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction', full_name='protoeth.TransactionInfo.transaction', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=178,
  serialized_end=216,
)


_TXRECEIPT = _descriptor.Descriptor(
  name='TxReceipt',
  full_name='protoeth.TxReceipt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txReceipt', full_name='protoeth.TxReceipt.txReceipt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=248,
)


_RAWTXREQUEST = _descriptor.Descriptor(
  name='RawTxRequest',
  full_name='protoeth.RawTxRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx', full_name='protoeth.RawTxRequest.tx', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=276,
)


_TXRESPONSE = _descriptor.Descriptor(
  name='TxResponse',
  full_name='protoeth.TxResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txData', full_name='protoeth.TxResponse.txData', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=306,
)

DESCRIPTOR.message_types_by_name['GetAccountsReq'] = _GETACCOUNTSREQ
DESCRIPTOR.message_types_by_name['GetAccountsResp'] = _GETACCOUNTSRESP
DESCRIPTOR.message_types_by_name['GetBalanceReq'] = _GETBALANCEREQ
DESCRIPTOR.message_types_by_name['GetBalanceResp'] = _GETBALANCERESP
DESCRIPTOR.message_types_by_name['TxHash'] = _TXHASH
DESCRIPTOR.message_types_by_name['TransactionInfo'] = _TRANSACTIONINFO
DESCRIPTOR.message_types_by_name['TxReceipt'] = _TXRECEIPT
DESCRIPTOR.message_types_by_name['RawTxRequest'] = _RAWTXREQUEST
DESCRIPTOR.message_types_by_name['TxResponse'] = _TXRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAccountsReq = _reflection.GeneratedProtocolMessageType('GetAccountsReq', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTSREQ,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.GetAccountsReq)
  })
_sym_db.RegisterMessage(GetAccountsReq)

GetAccountsResp = _reflection.GeneratedProtocolMessageType('GetAccountsResp', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTSRESP,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.GetAccountsResp)
  })
_sym_db.RegisterMessage(GetAccountsResp)

GetBalanceReq = _reflection.GeneratedProtocolMessageType('GetBalanceReq', (_message.Message,), {
  'DESCRIPTOR' : _GETBALANCEREQ,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.GetBalanceReq)
  })
_sym_db.RegisterMessage(GetBalanceReq)

GetBalanceResp = _reflection.GeneratedProtocolMessageType('GetBalanceResp', (_message.Message,), {
  'DESCRIPTOR' : _GETBALANCERESP,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.GetBalanceResp)
  })
_sym_db.RegisterMessage(GetBalanceResp)

TxHash = _reflection.GeneratedProtocolMessageType('TxHash', (_message.Message,), {
  'DESCRIPTOR' : _TXHASH,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.TxHash)
  })
_sym_db.RegisterMessage(TxHash)

TransactionInfo = _reflection.GeneratedProtocolMessageType('TransactionInfo', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONINFO,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.TransactionInfo)
  })
_sym_db.RegisterMessage(TransactionInfo)

TxReceipt = _reflection.GeneratedProtocolMessageType('TxReceipt', (_message.Message,), {
  'DESCRIPTOR' : _TXRECEIPT,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.TxReceipt)
  })
_sym_db.RegisterMessage(TxReceipt)

RawTxRequest = _reflection.GeneratedProtocolMessageType('RawTxRequest', (_message.Message,), {
  'DESCRIPTOR' : _RAWTXREQUEST,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.RawTxRequest)
  })
_sym_db.RegisterMessage(RawTxRequest)

TxResponse = _reflection.GeneratedProtocolMessageType('TxResponse', (_message.Message,), {
  'DESCRIPTOR' : _TXRESPONSE,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.TxResponse)
  })
_sym_db.RegisterMessage(TxResponse)


DESCRIPTOR._options = None

_PROTOETHSERVICE = _descriptor.ServiceDescriptor(
  name='ProtoEthService',
  full_name='protoeth.ProtoEthService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=309,
  serialized_end=667,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAccounts',
    full_name='protoeth.ProtoEthService.GetAccounts',
    index=0,
    containing_service=None,
    input_type=_GETACCOUNTSREQ,
    output_type=_GETACCOUNTSRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBalance',
    full_name='protoeth.ProtoEthService.GetBalance',
    index=1,
    containing_service=None,
    input_type=_GETBALANCEREQ,
    output_type=_GETBALANCERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTransaction',
    full_name='protoeth.ProtoEthService.GetTransaction',
    index=2,
    containing_service=None,
    input_type=_TXHASH,
    output_type=_TRANSACTIONINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendRawTransactions',
    full_name='protoeth.ProtoEthService.SendRawTransactions',
    index=3,
    containing_service=None,
    input_type=_RAWTXREQUEST,
    output_type=_TXRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTransactionReceipt',
    full_name='protoeth.ProtoEthService.GetTransactionReceipt',
    index=4,
    containing_service=None,
    input_type=_TXHASH,
    output_type=_TXRECEIPT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROTOETHSERVICE)

DESCRIPTOR.services_by_name['ProtoEthService'] = _PROTOETHSERVICE

# @@protoc_insertion_point(module_scope)
