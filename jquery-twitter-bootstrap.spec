#
# Conditional build:
%bcond_without	default	# use this version as default version (symlink)

%define		plugin	twitter-bootstrap
%define		altname	bootstrap
Summary:	Bootstrap - front-end framework for faster and easier web development
Name:		jquery-%{plugin}
Version:	3.1.1
Release:	1
License:	Apache License v2.0
Group:		Applications/WWW
Source0:	https://github.com/twbs/bootstrap/releases/download/v%{version}/bootstrap-%{version}-dist.zip
# Source0-md5:	6280e447a777c90440fbdca7c504fd9c
URL:		http://getbootstrap.com/
BuildRequires:	unzip
Requires:	jquery >= 1.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		jquerydir	%{_datadir}/jquery
%define		basedir	%{_datadir}/jquery/%{altname}
%define		_appdir	%{basedir}-3.1

%description
Sleek, intuitive, and powerful front-end framework for faster and
easier web development.

%prep
%setup -qn bootstrap-%{version}-dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}/{js,css}

cp -p js/%{altname}.js $RPM_BUILD_ROOT%{_appdir}/js/%{altname}-%{version}.js
cp -p js/%{altname}.min.js $RPM_BUILD_ROOT%{_appdir}/js/%{altname}-%{version}.min.js
ln -s %{altname}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/js/%{altname}.src.js
ln -s %{altname}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/js/%{altname}.js
ln -s %{altname}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/js/%{altname}.min.js

cp -p css/%{altname}.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-%{version}.css
cp -p css/%{altname}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-%{version}.min.css
cp -p css/%{altname}.css.map $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-%{version}.css.map
ln -s %{altname}-%{version}.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}.src.css
ln -s %{altname}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}.css
ln -s %{altname}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}.min.css
ln -s %{altname}-%{version}.css.map $RPM_BUILD_ROOT%{_appdir}/css/%{altname}.css.map

cp -p css/%{altname}-theme.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-theme-%{version}.css
cp -p css/%{altname}-theme.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-theme-%{version}.min.css
cp -p css/%{altname}-theme.css.map $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-theme-%{version}.css.map
ln -s %{altname}-theme-%{version}.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-theme.src.css
ln -s %{altname}-theme-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-theme.css
ln -s %{altname}-theme-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-theme.min.css
ln -s %{altname}-theme-%{version}.css.map $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-theme.css.map

cp -a fonts $RPM_BUILD_ROOT%{_appdir}

%if %{with default}
ln -s $(basename %{_appdir}) $RPM_BUILD_ROOT%{jquerydir}/%{altname}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
%if %{with default}
%{jquerydir}/%{altname}
%endif
