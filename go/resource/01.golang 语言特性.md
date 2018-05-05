## 语言特性


### 1、垃圾回收

- 内存自动回收
- 只需要new 分配内存，不需要释放
- 有个后台程序自动回收内存
- 开发效率之所以这么高的原因

### 2、天然并发

- 从语言层面支持并发，非常简单
- goroute 轻量级县城 创建成千上万goroute 成为可能
- 给予csp 模型实现（communicating sequential process）
