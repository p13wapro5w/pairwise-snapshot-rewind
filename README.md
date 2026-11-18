# pairwise-snapshot-rewind

联机对枪时敌人瞬移、回滚、子弹穿墙：快照插值用到达时间不是服务器 tick；缓冲不足时直接外推；位置和旋转分别插值导致不同步；lag compensation 回滚只回滚玩家不回滚门；丢包时快照乱序；时钟漂移没校正；本地预测和权威状态硬切；子弹命中用当前位置不是回滚位置；高延迟玩家看到的血条和实际不同；插值步长随渲染帧变。net/snapshot_interp.py 是核心，tests/test_snapshot_interp.py 15个红。要修的是：按 tick 插值；外推限幅；位姿同步；全场景回滚；序号缓冲；时钟同步；预测混合；回滚位置命中；延迟一致 UI；固定插值步长。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：游戏开发；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
