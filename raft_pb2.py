# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raft.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nraft.proto\">\n\x05\x65ntry\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x0c\n\x04term\x18\x02 \x01(\x05\x12\x0b\n\x03key\x18\x03 \x01(\x05\x12\x0b\n\x03val\x18\x04 \x01(\x05\"\xa4\x01\n\x11\x41ppendEntriesArgs\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x10\n\x08leaderId\x18\x02 \x01(\x05\x12\x14\n\x0cprevLogIndex\x18\x03 \x01(\x05\x12\x13\n\x0bprevLogTerm\x18\x04 \x01(\x05\x12\x17\n\x07\x65ntries\x18\x05 \x03(\x0b\x32\x06.entry\x12\x14\n\x0cleaderCommit\x18\x06 \x01(\x05\x12\x15\n\rleaseInterval\x18\x07 \x01(\x05\"1\n\x10\x41ppendEntriesRes\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0f\n\x07success\x18\x02 \x01(\x08\"`\n\x10RequestVotesArgs\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x13\n\x0b\x63\x61ndidateId\x18\x02 \x01(\x05\x12\x14\n\x0clastLogIndex\x18\x03 \x01(\x05\x12\x13\n\x0blastLogTerm\x18\x04 \x01(\x05\"`\n\x0fRequestVotesRes\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x13\n\x0bvoteGranted\x18\x02 \x01(\x08\x12\x1a\n\x12longestDurationRem\x18\x03 \x01(\x05\x12\x0e\n\x06NodeId\x18\x04 \x01(\x05\"\"\n\x0fServeClientArgs\x12\x0f\n\x07Request\x18\x01 \x01(\t\"C\n\x10ServeClientReply\x12\x0c\n\x04\x44\x61ta\x18\x01 \x01(\t\x12\x10\n\x08LeaderID\x18\x02 \x01(\t\x12\x0f\n\x07Success\x18\x03 \x01(\x08\"\x8e\x01\n\x10ReplicateLogArgs\x12\x10\n\x08leaderId\x18\x01 \x01(\x05\x12\x13\n\x0b\x63urrentTerm\x18\x02 \x01(\x05\x12\x11\n\tprefixLen\x18\x03 \x01(\x05\x12\x12\n\nprefixTerm\x18\x04 \x01(\x05\x12\x14\n\x0c\x63ommitLength\x18\x05 \x01(\x05\x12\x16\n\x06suffix\x18\x06 \x03(\x0b\x32\x06.entry\"_\n\x0fReplicateLogRes\x12\x0e\n\x06nodeId\x18\x01 \x01(\x05\x12\x13\n\x0b\x63urrentTerm\x18\x02 \x01(\x05\x12\x0e\n\x06\x61\x63kLen\x18\x03 \x01(\x05\x12\x17\n\x0freceivedMessage\x18\x04 \x01(\x08\x32\xe3\x01\n\x04Raft\x12\x38\n\rAppendEntries\x12\x12.AppendEntriesArgs\x1a\x11.AppendEntriesRes\"\x00\x12\x34\n\x0bRequestVote\x12\x11.RequestVotesArgs\x1a\x10.RequestVotesRes\"\x00\x12\x34\n\x0bServeClient\x12\x10.ServeClientArgs\x1a\x11.ServeClientReply\"\x00\x12\x35\n\x0cReplicateLog\x12\x11.ReplicateLogArgs\x1a\x10.ReplicateLogRes\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'raft_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ENTRY']._serialized_start=14
  _globals['_ENTRY']._serialized_end=76
  _globals['_APPENDENTRIESARGS']._serialized_start=79
  _globals['_APPENDENTRIESARGS']._serialized_end=243
  _globals['_APPENDENTRIESRES']._serialized_start=245
  _globals['_APPENDENTRIESRES']._serialized_end=294
  _globals['_REQUESTVOTESARGS']._serialized_start=296
  _globals['_REQUESTVOTESARGS']._serialized_end=392
  _globals['_REQUESTVOTESRES']._serialized_start=394
  _globals['_REQUESTVOTESRES']._serialized_end=490
  _globals['_SERVECLIENTARGS']._serialized_start=492
  _globals['_SERVECLIENTARGS']._serialized_end=526
  _globals['_SERVECLIENTREPLY']._serialized_start=528
  _globals['_SERVECLIENTREPLY']._serialized_end=595
  _globals['_REPLICATELOGARGS']._serialized_start=598
  _globals['_REPLICATELOGARGS']._serialized_end=740
  _globals['_REPLICATELOGRES']._serialized_start=742
  _globals['_REPLICATELOGRES']._serialized_end=837
  _globals['_RAFT']._serialized_start=840
  _globals['_RAFT']._serialized_end=1067
# @@protoc_insertion_point(module_scope)
