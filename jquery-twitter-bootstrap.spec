Summary:	Bootstrap - front-end framework for faster and easier web development
Name:		twitter-bootstrap
Version:	2.1.0
Release:	0.1
License:	Apache License v2.0
Group:		Applications/WWW
Source0:	http://twitter.github.com/bootstrap/assets/bootstrap.zip
# Source0-md5:	1ae7b16761a8097dc78679a5dacc0ab7
URL:		http://twitter.github.com/bootstrap/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sleek, intuitive, and powerful front-end framework for faster and
easier web development.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
