from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerAction(_message.Message):
    __slots__ = ("player_id", "dx", "dy")
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    DX_FIELD_NUMBER: _ClassVar[int]
    DY_FIELD_NUMBER: _ClassVar[int]
    player_id: str
    dx: int
    dy: int
    def __init__(self, player_id: _Optional[str] = ..., dx: _Optional[int] = ..., dy: _Optional[int] = ...) -> None: ...

class ViewRequest(_message.Message):
    __slots__ = ("player_id",)
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    player_id: str
    def __init__(self, player_id: _Optional[str] = ...) -> None: ...

class Cell(_message.Message):
    __slots__ = ("pseudo", "role", "x", "y")
    PSEUDO_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    pseudo: str
    role: str
    x: int
    y: int
    def __init__(self, pseudo: _Optional[str] = ..., role: _Optional[str] = ..., x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class MoveResponse(_message.Message):
    __slots__ = ("success", "message", "new_x", "new_y", "visible_cells")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NEW_X_FIELD_NUMBER: _ClassVar[int]
    NEW_Y_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_CELLS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    new_x: int
    new_y: int
    visible_cells: _containers.RepeatedCompositeFieldContainer[Cell]
    def __init__(self, success: bool = ..., message: _Optional[str] = ..., new_x: _Optional[int] = ..., new_y: _Optional[int] = ..., visible_cells: _Optional[_Iterable[_Union[Cell, _Mapping]]] = ...) -> None: ...

class ViewResponse(_message.Message):
    __slots__ = ("visible_cells",)
    VISIBLE_CELLS_FIELD_NUMBER: _ClassVar[int]
    visible_cells: _containers.RepeatedCompositeFieldContainer[Cell]
    def __init__(self, visible_cells: _Optional[_Iterable[_Union[Cell, _Mapping]]] = ...) -> None: ...
