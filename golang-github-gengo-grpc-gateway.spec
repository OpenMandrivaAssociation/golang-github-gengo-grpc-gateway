# http://github.com/gengo/grpc-gateway
%global goipath         github.com/gengo/grpc-gateway
%global commit          dcb844349dc5d2cb0300fdc4d2d374839d0d2e13

%gometa -i

Name:           %{goname}
Version:        0
Release:        0.8%{?dist}
Summary:        GRPC to JSON proxy generator
# Detected licences
# - BSD (3 clause) at 'LICENSE.txt'
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/golang/glog)
BuildRequires: golang(github.com/golang/protobuf/jsonpb)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/generator)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/plugin)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/grpclog)
BuildRequires: golang(google.golang.org/grpc/metadata)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup

%install
%goinstall

%check
%gochecks -d runtime

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE.txt
%doc README.md

%changelog
* Wed Sep 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.8.gitdcb8443
- Polish spec file
  resolves: #1555797

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.6.20160614gitdcb8443
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitdcb8443
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitdcb8443
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitdcb8443
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitdcb8443
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 11 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.gitdcb8443
- First package for Fedora
  resolves: #1354375
