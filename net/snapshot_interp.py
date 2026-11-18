"""第 52 批：联机对枪时敌人瞬移、回滚、子弹穿墙：快照插值用到..."""

def tick_alpha(render_tick, prev_tick, next_tick):
    """按服务器 tick 返回插值系数。"""
    raise NotImplementedError("TODO: tick_alpha")

def clamp_extrapolation(delta, max_delta):
    """限制快照外推距离。"""
    raise NotImplementedError("TODO: clamp_extrapolation")

def pose_sync(position, rotation):
    """返回同步后的位姿。"""
    raise NotImplementedError("TODO: pose_sync")

def rollback_world(players, doors):
    """返回包含玩家与门的回滚状态。"""
    raise NotImplementedError("TODO: rollback_world")

def sequence_ok(seq, last_seq):
    """判断快照序号是否按序到达。"""
    raise NotImplementedError("TODO: sequence_ok")

def clock_offset(local_time, remote_time):
    """返回本地与服务器时钟偏移。"""
    raise NotImplementedError("TODO: clock_offset")

def blend_prediction(authority, predicted, alpha):
    """在权威状态与预测状态之间插值。"""
    raise NotImplementedError("TODO: blend_prediction")

def hit_at_rewind(current_pos, rewind_pos):
    """返回命中检测使用的回滚位置。"""
    raise NotImplementedError("TODO: hit_at_rewind")
