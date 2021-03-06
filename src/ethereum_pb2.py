# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethereum.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ethereum.proto',
  package='protoeth',
  syntax='proto3',
  serialized_options=_b('Z\010protoeth'),
  serialized_pb=_b('\n\x0e\x65thereum.proto\x12\x08protoeth\x1a\x1bgoogle/protobuf/empty.proto\"\x10\n\x0eGetAccountsReq\"\x18\n\nTestnetReq\x12\n\n\x02id\x18\x01 \x01(\r\"7\n\x12HashStringOrNumber\x12\x11\n\treqString\x18\x01 \x01(\t\x12\x0e\n\x06reqNum\x18\x02 \x01(\x04\"I\n\rInfoWithIndex\x12)\n\x03req\x18\x01 \x01(\x0b\x32\x1c.protoeth.HashStringOrNumber\x12\r\n\x05index\x18\x02 \x01(\x04\"\x1a\n\tCountResp\x12\r\n\x05\x63ount\x18\x01 \x01(\x04\"\x1a\n\x07ObjResp\x12\x0f\n\x07respObj\x18\x01 \x01(\t\"#\n\x0fGetAccountsResp\x12\x10\n\x08\x61\x63\x63ounts\x18\x01 \x03(\t\" \n\rGetBalanceReq\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"!\n\x0eGetBalanceResp\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\t\"O\n\x17\x43reateRawTransactionReq\x12\n\n\x02to\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x0b\n\x03gas\x18\x03 \x01(\r\x12\r\n\x05value\x18\x04 \x01(\r\")\n\x18\x43reateRawTransactionResp\x12\r\n\x05rawTX\x18\x01 \x01(\t\".\n\x1a\x44\x65ploySignedTransactionReq\x12\x10\n\x08signedTX\x18\x01 \x01(\t\"0\n\x1b\x44\x65ploySignedTransactionResp\x12\x11\n\ttxReciept\x18\x01 \x01(\t\"\x18\n\x06TxHash\x12\x0e\n\x06txhash\x18\x01 \x01(\t\"&\n\x0fTransactionInfo\x12\x13\n\x0btransaction\x18\x01 \x01(\t\"\x1e\n\tTxReceipt\x12\x11\n\ttxReceipt\x18\x01 \x01(\t\"-\n\x0cRawTxRequest\x12\x11\n\tnetworkid\x18\x01 \x01(\r\x12\n\n\x02tx\x18\x02 \x01(\t\"\x1f\n\x0b\x42lockNumber\x12\x10\n\x08\x62locknum\x18\x01 \x01(\x04\"\x1c\n\nTxResponse\x12\x0e\n\x06txData\x18\x01 \x01(\t\"\x1e\n\tNumResult\x12\x11\n\tresultNum\x18\x01 \x01(\x04\"-\n\x08GetTxReq\x12\x11\n\tnetworkid\x18\x01 \x01(\r\x12\x0e\n\x06txhash\x18\x02 \x01(\t\"\x91\x01\n\x0b\x43\x61llRequest\x12\x11\n\tnetworkid\x18\x01 \x01(\r\x12\n\n\x02\x66n\x18\x02 \x01(\t\x12\x0e\n\x06params\x18\x03 \x01(\t\x12\x0b\n\x03\x61\x62i\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\t\x12\x13\n\x0b\x66romAddress\x18\x06 \x01(\t\x12\r\n\x05value\x18\x07 \x01(\x04\x12\x11\n\tgasSupply\x18\x08 \x01(\x04\"\x1e\n\x0c\x43\x61llResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2\xf9\x05\n\x0fProtoEthService\x12\x41\n\nGetBalance\x12\x17.protoeth.GetBalanceReq\x1a\x18.protoeth.GetBalanceResp\"\x00\x12\x41\n\x0eGetTransaction\x12\x12.protoeth.GetTxReq\x1a\x19.protoeth.TransactionInfo\"\x00\x12@\n\x15GetTransactionReceipt\x12\x10.protoeth.TxHash\x1a\x13.protoeth.TxReceipt\"\x00\x12?\n\x0c\x43ontractCall\x12\x15.protoeth.CallRequest\x1a\x16.protoeth.CallResponse\"\x00\x12<\n\x0bGetHashrate\x12\x16.google.protobuf.Empty\x1a\x13.protoeth.NumResult\"\x00\x12<\n\x0bGetGasPrice\x12\x16.google.protobuf.Empty\x1a\x13.protoeth.NumResult\"\x00\x12\x41\n\x0eGetBlockNumber\x12\x16.google.protobuf.Empty\x1a\x15.protoeth.BlockNumber\"\x00\x12O\n\x18GetBlockTransactionCount\x12\x1c.protoeth.HashStringOrNumber\x1a\x13.protoeth.CountResp\"\x00\x12=\n\x08GetBlock\x12\x1c.protoeth.HashStringOrNumber\x1a\x11.protoeth.ObjResp\"\x00\x12G\n\x17GetTransactionFromBlock\x12\x17.protoeth.InfoWithIndex\x1a\x11.protoeth.ObjResp\"\x00\x12\x45\n\x13SendRawTransactions\x12\x16.protoeth.RawTxRequest\x1a\x14.protoeth.TxResponse\"\x00\x42\nZ\x08protoethb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




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
  serialized_start=57,
  serialized_end=73,
)


_TESTNETREQ = _descriptor.Descriptor(
  name='TestnetReq',
  full_name='protoeth.TestnetReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protoeth.TestnetReq.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=75,
  serialized_end=99,
)


_HASHSTRINGORNUMBER = _descriptor.Descriptor(
  name='HashStringOrNumber',
  full_name='protoeth.HashStringOrNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reqString', full_name='protoeth.HashStringOrNumber.reqString', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reqNum', full_name='protoeth.HashStringOrNumber.reqNum', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=101,
  serialized_end=156,
)


_INFOWITHINDEX = _descriptor.Descriptor(
  name='InfoWithIndex',
  full_name='protoeth.InfoWithIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='req', full_name='protoeth.InfoWithIndex.req', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='protoeth.InfoWithIndex.index', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=158,
  serialized_end=231,
)


_COUNTRESP = _descriptor.Descriptor(
  name='CountResp',
  full_name='protoeth.CountResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='protoeth.CountResp.count', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=233,
  serialized_end=259,
)


_OBJRESP = _descriptor.Descriptor(
  name='ObjResp',
  full_name='protoeth.ObjResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='respObj', full_name='protoeth.ObjResp.respObj', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=261,
  serialized_end=287,
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
  serialized_start=289,
  serialized_end=324,
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
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=326,
  serialized_end=358,
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
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=360,
  serialized_end=393,
)


_CREATERAWTRANSACTIONREQ = _descriptor.Descriptor(
  name='CreateRawTransactionReq',
  full_name='protoeth.CreateRawTransactionReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='to', full_name='protoeth.CreateRawTransactionReq.to', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='protoeth.CreateRawTransactionReq.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas', full_name='protoeth.CreateRawTransactionReq.gas', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protoeth.CreateRawTransactionReq.value', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=395,
  serialized_end=474,
)


_CREATERAWTRANSACTIONRESP = _descriptor.Descriptor(
  name='CreateRawTransactionResp',
  full_name='protoeth.CreateRawTransactionResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rawTX', full_name='protoeth.CreateRawTransactionResp.rawTX', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=476,
  serialized_end=517,
)


_DEPLOYSIGNEDTRANSACTIONREQ = _descriptor.Descriptor(
  name='DeploySignedTransactionReq',
  full_name='protoeth.DeploySignedTransactionReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signedTX', full_name='protoeth.DeploySignedTransactionReq.signedTX', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=519,
  serialized_end=565,
)


_DEPLOYSIGNEDTRANSACTIONRESP = _descriptor.Descriptor(
  name='DeploySignedTransactionResp',
  full_name='protoeth.DeploySignedTransactionResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txReciept', full_name='protoeth.DeploySignedTransactionResp.txReciept', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=567,
  serialized_end=615,
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
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=617,
  serialized_end=641,
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
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=643,
  serialized_end=681,
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
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=683,
  serialized_end=713,
)


_RAWTXREQUEST = _descriptor.Descriptor(
  name='RawTxRequest',
  full_name='protoeth.RawTxRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='networkid', full_name='protoeth.RawTxRequest.networkid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx', full_name='protoeth.RawTxRequest.tx', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=715,
  serialized_end=760,
)


_BLOCKNUMBER = _descriptor.Descriptor(
  name='BlockNumber',
  full_name='protoeth.BlockNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blocknum', full_name='protoeth.BlockNumber.blocknum', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=762,
  serialized_end=793,
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
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=795,
  serialized_end=823,
)


_NUMRESULT = _descriptor.Descriptor(
  name='NumResult',
  full_name='protoeth.NumResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultNum', full_name='protoeth.NumResult.resultNum', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=825,
  serialized_end=855,
)


_GETTXREQ = _descriptor.Descriptor(
  name='GetTxReq',
  full_name='protoeth.GetTxReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='networkid', full_name='protoeth.GetTxReq.networkid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txhash', full_name='protoeth.GetTxReq.txhash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=857,
  serialized_end=902,
)


_CALLREQUEST = _descriptor.Descriptor(
  name='CallRequest',
  full_name='protoeth.CallRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='networkid', full_name='protoeth.CallRequest.networkid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fn', full_name='protoeth.CallRequest.fn', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='protoeth.CallRequest.params', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abi', full_name='protoeth.CallRequest.abi', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='protoeth.CallRequest.address', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fromAddress', full_name='protoeth.CallRequest.fromAddress', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protoeth.CallRequest.value', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gasSupply', full_name='protoeth.CallRequest.gasSupply', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=905,
  serialized_end=1050,
)


_CALLRESPONSE = _descriptor.Descriptor(
  name='CallResponse',
  full_name='protoeth.CallResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='protoeth.CallResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1052,
  serialized_end=1082,
)

_INFOWITHINDEX.fields_by_name['req'].message_type = _HASHSTRINGORNUMBER
DESCRIPTOR.message_types_by_name['GetAccountsReq'] = _GETACCOUNTSREQ
DESCRIPTOR.message_types_by_name['TestnetReq'] = _TESTNETREQ
DESCRIPTOR.message_types_by_name['HashStringOrNumber'] = _HASHSTRINGORNUMBER
DESCRIPTOR.message_types_by_name['InfoWithIndex'] = _INFOWITHINDEX
DESCRIPTOR.message_types_by_name['CountResp'] = _COUNTRESP
DESCRIPTOR.message_types_by_name['ObjResp'] = _OBJRESP
DESCRIPTOR.message_types_by_name['GetAccountsResp'] = _GETACCOUNTSRESP
DESCRIPTOR.message_types_by_name['GetBalanceReq'] = _GETBALANCEREQ
DESCRIPTOR.message_types_by_name['GetBalanceResp'] = _GETBALANCERESP
DESCRIPTOR.message_types_by_name['CreateRawTransactionReq'] = _CREATERAWTRANSACTIONREQ
DESCRIPTOR.message_types_by_name['CreateRawTransactionResp'] = _CREATERAWTRANSACTIONRESP
DESCRIPTOR.message_types_by_name['DeploySignedTransactionReq'] = _DEPLOYSIGNEDTRANSACTIONREQ
DESCRIPTOR.message_types_by_name['DeploySignedTransactionResp'] = _DEPLOYSIGNEDTRANSACTIONRESP
DESCRIPTOR.message_types_by_name['TxHash'] = _TXHASH
DESCRIPTOR.message_types_by_name['TransactionInfo'] = _TRANSACTIONINFO
DESCRIPTOR.message_types_by_name['TxReceipt'] = _TXRECEIPT
DESCRIPTOR.message_types_by_name['RawTxRequest'] = _RAWTXREQUEST
DESCRIPTOR.message_types_by_name['BlockNumber'] = _BLOCKNUMBER
DESCRIPTOR.message_types_by_name['TxResponse'] = _TXRESPONSE
DESCRIPTOR.message_types_by_name['NumResult'] = _NUMRESULT
DESCRIPTOR.message_types_by_name['GetTxReq'] = _GETTXREQ
DESCRIPTOR.message_types_by_name['CallRequest'] = _CALLREQUEST
DESCRIPTOR.message_types_by_name['CallResponse'] = _CALLRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAccountsReq = _reflection.GeneratedProtocolMessageType('GetAccountsReq', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTSREQ,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.GetAccountsReq)
  })
_sym_db.RegisterMessage(GetAccountsReq)

TestnetReq = _reflection.GeneratedProtocolMessageType('TestnetReq', (_message.Message,), {
  'DESCRIPTOR' : _TESTNETREQ,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.TestnetReq)
  })
_sym_db.RegisterMessage(TestnetReq)

HashStringOrNumber = _reflection.GeneratedProtocolMessageType('HashStringOrNumber', (_message.Message,), {
  'DESCRIPTOR' : _HASHSTRINGORNUMBER,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.HashStringOrNumber)
  })
_sym_db.RegisterMessage(HashStringOrNumber)

InfoWithIndex = _reflection.GeneratedProtocolMessageType('InfoWithIndex', (_message.Message,), {
  'DESCRIPTOR' : _INFOWITHINDEX,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.InfoWithIndex)
  })
_sym_db.RegisterMessage(InfoWithIndex)

CountResp = _reflection.GeneratedProtocolMessageType('CountResp', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRESP,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.CountResp)
  })
_sym_db.RegisterMessage(CountResp)

ObjResp = _reflection.GeneratedProtocolMessageType('ObjResp', (_message.Message,), {
  'DESCRIPTOR' : _OBJRESP,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.ObjResp)
  })
_sym_db.RegisterMessage(ObjResp)

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

CreateRawTransactionReq = _reflection.GeneratedProtocolMessageType('CreateRawTransactionReq', (_message.Message,), {
  'DESCRIPTOR' : _CREATERAWTRANSACTIONREQ,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.CreateRawTransactionReq)
  })
_sym_db.RegisterMessage(CreateRawTransactionReq)

CreateRawTransactionResp = _reflection.GeneratedProtocolMessageType('CreateRawTransactionResp', (_message.Message,), {
  'DESCRIPTOR' : _CREATERAWTRANSACTIONRESP,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.CreateRawTransactionResp)
  })
_sym_db.RegisterMessage(CreateRawTransactionResp)

DeploySignedTransactionReq = _reflection.GeneratedProtocolMessageType('DeploySignedTransactionReq', (_message.Message,), {
  'DESCRIPTOR' : _DEPLOYSIGNEDTRANSACTIONREQ,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.DeploySignedTransactionReq)
  })
_sym_db.RegisterMessage(DeploySignedTransactionReq)

DeploySignedTransactionResp = _reflection.GeneratedProtocolMessageType('DeploySignedTransactionResp', (_message.Message,), {
  'DESCRIPTOR' : _DEPLOYSIGNEDTRANSACTIONRESP,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.DeploySignedTransactionResp)
  })
_sym_db.RegisterMessage(DeploySignedTransactionResp)

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

BlockNumber = _reflection.GeneratedProtocolMessageType('BlockNumber', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKNUMBER,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.BlockNumber)
  })
_sym_db.RegisterMessage(BlockNumber)

TxResponse = _reflection.GeneratedProtocolMessageType('TxResponse', (_message.Message,), {
  'DESCRIPTOR' : _TXRESPONSE,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.TxResponse)
  })
_sym_db.RegisterMessage(TxResponse)

NumResult = _reflection.GeneratedProtocolMessageType('NumResult', (_message.Message,), {
  'DESCRIPTOR' : _NUMRESULT,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.NumResult)
  })
_sym_db.RegisterMessage(NumResult)

GetTxReq = _reflection.GeneratedProtocolMessageType('GetTxReq', (_message.Message,), {
  'DESCRIPTOR' : _GETTXREQ,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.GetTxReq)
  })
_sym_db.RegisterMessage(GetTxReq)

CallRequest = _reflection.GeneratedProtocolMessageType('CallRequest', (_message.Message,), {
  'DESCRIPTOR' : _CALLREQUEST,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.CallRequest)
  })
_sym_db.RegisterMessage(CallRequest)

CallResponse = _reflection.GeneratedProtocolMessageType('CallResponse', (_message.Message,), {
  'DESCRIPTOR' : _CALLRESPONSE,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.CallResponse)
  })
_sym_db.RegisterMessage(CallResponse)


DESCRIPTOR._options = None

_PROTOETHSERVICE = _descriptor.ServiceDescriptor(
  name='ProtoEthService',
  full_name='protoeth.ProtoEthService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1085,
  serialized_end=1846,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBalance',
    full_name='protoeth.ProtoEthService.GetBalance',
    index=0,
    containing_service=None,
    input_type=_GETBALANCEREQ,
    output_type=_GETBALANCERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTransaction',
    full_name='protoeth.ProtoEthService.GetTransaction',
    index=1,
    containing_service=None,
    input_type=_GETTXREQ,
    output_type=_TRANSACTIONINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTransactionReceipt',
    full_name='protoeth.ProtoEthService.GetTransactionReceipt',
    index=2,
    containing_service=None,
    input_type=_TXHASH,
    output_type=_TXRECEIPT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ContractCall',
    full_name='protoeth.ProtoEthService.ContractCall',
    index=3,
    containing_service=None,
    input_type=_CALLREQUEST,
    output_type=_CALLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetHashrate',
    full_name='protoeth.ProtoEthService.GetHashrate',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_NUMRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetGasPrice',
    full_name='protoeth.ProtoEthService.GetGasPrice',
    index=5,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_NUMRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBlockNumber',
    full_name='protoeth.ProtoEthService.GetBlockNumber',
    index=6,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_BLOCKNUMBER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBlockTransactionCount',
    full_name='protoeth.ProtoEthService.GetBlockTransactionCount',
    index=7,
    containing_service=None,
    input_type=_HASHSTRINGORNUMBER,
    output_type=_COUNTRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBlock',
    full_name='protoeth.ProtoEthService.GetBlock',
    index=8,
    containing_service=None,
    input_type=_HASHSTRINGORNUMBER,
    output_type=_OBJRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTransactionFromBlock',
    full_name='protoeth.ProtoEthService.GetTransactionFromBlock',
    index=9,
    containing_service=None,
    input_type=_INFOWITHINDEX,
    output_type=_OBJRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendRawTransactions',
    full_name='protoeth.ProtoEthService.SendRawTransactions',
    index=10,
    containing_service=None,
    input_type=_RAWTXREQUEST,
    output_type=_TXRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROTOETHSERVICE)

DESCRIPTOR.services_by_name['ProtoEthService'] = _PROTOETHSERVICE

# @@protoc_insertion_point(module_scope)
