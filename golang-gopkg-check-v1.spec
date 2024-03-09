%global debug_package %{nil}

# Run tests in check section
%bcond_without check

# https://github.com/go-check/check
%global goipath		gopkg.in/check.v1
%global forgeurl	https://github.com/go-check/check
%global commit          10cb98267c6cb43ea9cd6793f29ff4089c306974
%global commitdate	20201130

%gometa

Summary:	Rich testing for the Go language
Name:		golang-gopkg-check-v1
Version:	1
Release:	%{?snapshot:0.git%{commitdate}.}1
Source0:	https://github.com/go-check/check/archive/v%{version}/check-%{version}.tar.gz
URL:		https://github.com/go-check/check
License:	BSD with attribution
Group:		Development/Other
BuildRequires:	compiler(go-compiler)

%description
Rich testing for the Go language. 

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md TODO

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n check-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

