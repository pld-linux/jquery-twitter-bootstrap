%define		plugin	twitter-bootstrap
%define		altname	bootstrap
Summary:	Bootstrap - front-end framework for faster and easier web development
Name:		jquery-%{plugin}
Version:	2.3.1
Release:	1
License:	Apache License v2.0
Group:		Applications/WWW
Source0:	http://twitter.github.com/bootstrap/assets/bootstrap.zip?/%{plugin}-%{version}.zip
# Source0-md5:	99a94c7ced6527822470f9d9f5a58681
URL:		http://twitter.github.io/bootstrap/
BuildRequires:	unzip
Requires:	jquery >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Sleek, intuitive, and powerful front-end framework for faster and
easier web development.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}/{js,css}

cp -p %{altname}/js/%{altname}.js $RPM_BUILD_ROOT%{_appdir}/js/%{altname}-%{version}.js
cp -p %{altname}/js/%{altname}.min.js $RPM_BUILD_ROOT%{_appdir}/js/%{altname}-%{version}.min.js
ln -s %{altname}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/js/%{altname}.src.js
ln -s %{altname}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/js/%{altname}.js
ln -s %{altname}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/js/%{altname}.min.js

cp -p %{altname}/css/%{altname}.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-%{version}.css
cp -p %{altname}/css/%{altname}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-%{version}.min.css
ln -s %{altname}-%{version}.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}.src.css
ln -s %{altname}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}.css
ln -s %{altname}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}.min.css

cp -p %{altname}/css/%{altname}-responsive.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-responsive-%{version}.css
cp -p %{altname}/css/%{altname}-responsive.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-responsive-%{version}.min.css
ln -s %{altname}-responsive-%{version}.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-responsive.src.css
ln -s %{altname}-responsive-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-responsive.css
ln -s %{altname}-responsive-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-responsive.min.css

cp -a %{altname}/img $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
