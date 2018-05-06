# Go
Go是一种新的语言，一种并发的、带垃圾回收的、快速编译的语言。它具有以下特点：
- 它可以在一台计算机上用几秒钟的时间编译一个大型的Go程序。
- Go为软件构造提供了一种模型，它使依赖分析更加容易，且避免了大部分C风格include文件与库的开头。
- Go是静态类型的语言，它的类型系统没有层级。因此用户不需要在定义类型之间的关系上花费时间，这样感觉起来比典型的面向对象语言更轻量级。
- Go完全是垃圾回收型的语言，并为并发执行与通信提供了基本的支持。
- 按照其设计，Go打算为多核机器上系统软件的构造提供一种方法。

Go是一种编译型语言，它结合了解释型语言的游刃有余，动态类型语言的开发效率，以及静态类型的安全性。它也打算成为现代的，支持网络与多核计算的语言。要满足这些目标，需要解决一些语言上的问题：一个富有表达能力但轻量级的类型系统，并发与垃圾回收机制，严格的依赖规范等等。这些无法通过库或工具解决好，因此Go也就应运而生了。



# install go && vscode配置


## 1、download go.pkg
```
https://golang.org/doc/install?download=go1.10.2.darwin-amd64.pkg
```

## 2、install go

one by one

## 3、Vs code configure go path

```
{
    "go.gopath": "/Users/lishulong/go"
}

```


```
Installing 9 tools at /usr/local/go/bin
  gocode
  gopkgs
  go-outline
  go-symbols
  guru
  gorename
  godef
  goreturns
  golint

Installing github.com/nsf/gocode FAILED
Installing github.com/uudashr/gopkgs/cmd/gopkgs FAILED
Installing github.com/ramya-rao-a/go-outline FAILED
Installing github.com/acroca/go-symbols FAILED
Installing golang.org/x/tools/cmd/guru FAILED
Installing golang.org/x/tools/cmd/guru FAILED
Installing golang.org/x/tools/cmd/gorename FAILED
Installing github.com/rogpeppe/godef FAILED


```
### 4、安装失败的解决方式

###### 查看配置
```
➜  ~ go env
GOARCH="amd64"
GOBIN=""
GOCACHE="/Users/lishulong/Library/Caches/go-build"
GOEXE=""
GOHOSTARCH="amd64"
GOHOSTOS="darwin"
GOOS="darwin"
GOPATH="/Users/lishulong/go"
GORACE=""
GOROOT="/usr/local/go"
GOTMPDIR=""
GOTOOLDIR="/usr/local/go/pkg/tool/darwin_amd64"
GCCGO="gccgo"
CC="clang"
CXX="clang++"
CGO_ENABLED="1"
CGO_CFLAGS="-g -O2"
CGO_CPPFLAGS=""
CGO_CXXFLAGS="-g -O2"
CGO_FFLAGS="-g -O2"
CGO_LDFLAGS="-g -O2"
PKG_CONFIG="pkg-config"
GOGCCFLAGS="-fPIC -m64 -pthread -fno-caret-diagnostics -Qunused-arguments -fmessage-length=0 -fdebug-prefix-map=/var/folders/9p/zpk45xz549s2w1m32h534p2c0000gn/T/go-build953280813=/tmp/go-build -gno-record-gcc-switches -fno-common"
➜  ~ 
```
###### 配置环境变量

```
 58 GOPATH="/Users/lishulong/go"
 59 export GOPATH=$GOPATH
 60 export PATH=$PATH:$GOPATH/bin
~                                                                                                                                                                                                           
".bash_profile" [readonly] 60L, 2006C  
```
### 5、VS code 安装包

###### An extension for VS Code which provides support for the Go language. 
```
https://github.com/Microsoft/vscode-go/wiki/Release-Notes
```



```
go get -u -v github.com/bytbox/golint 
go get -u -v github.com/golang/tools 
go get -u -v github.com/lukehoban/go-outline 
go get -u -v github.com/newhook/go-symbols 
go get -u -v github.com/josharian/impl 
go get -u -v github.com/sqs/goreturns 
go get -u -v github.com/cweill/gotests
```
