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








```
作曲 : 深七

作词 : 深七

你要我怎么做怎么说你才能爱我

要我唱几首歌才能够将你捕捉

你要我怎么做怎么说你才能爱我

要我唱几首歌才能够将你捕捉

或许我太渺小 有几分傲

让我们抱一抱 好不好 世界太吵

你是场不散的 感人电影 温暖风景

酒多愁才清醒 才能够 爬你的山顶

路上走的小孩 总是稀奇古怪

看不清的阴霾 赤脚还相信爱

酸甜苦辣世界 对不起与谢谢

余生和你的夜 不会让它毁灭

想起你姑娘~ 微笑起来的模样

想起你姑娘~ 走在未来路上

想起你姑娘~ 昨天不会遗忘

想起你姑娘~ 想起你姑娘

你要我怎么做怎么说你才能爱我

要我唱几首歌才能够将你捕捉

你要我怎么做怎么说你才能爱我

要我唱几首歌才能够将你捕捉

或许我太渺小 有几分傲

让我们抱一抱 好不好 世界太吵

你是场不散的 感人电影 温暖风景

酒多愁才清醒 才能够 爬你的山顶

```