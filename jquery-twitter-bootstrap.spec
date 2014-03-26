#
# Conditional build:
%bcond_without	default	# use this version as default version (symlink)

%define		plugin	twitter-bootstrap
%define		altname	bootstrap
Summary:	Bootstrap - front-end framework for faster and easier web development
Name:		jquery-%{plugin}
Version:	2.3.2
Release:	1
License:	Apache License v2.0
Group:		Applications/WWW
Source0:	http://getbootstrap.com/%{version}/assets/bootstrap.zip?/%{plugin}-%{version}.zip
# Source0-md5:	2b2df1b111dfb560e7b0a1f1b8e0743a
URL:		http://twitter.github.io/bootstrap/
BuildRequires:	unzip
Requires:	jquery >= 1.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		jquerydir	%{_datadir}/jquery
%define		basedir	%{_datadir}/jquery/%{altname}
%define		_appdir	%{basedir}-2.3

%description
Sleek, intuitive, and powerful front-end framework for faster and
easier web development.

%prep
%setup -qc
mv %{altname}/* .

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
ln -s %{altname}-%{version}.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}.src.css
ln -s %{altname}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}.css
ln -s %{altname}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}.min.css

cp -p css/%{altname}-responsive.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-responsive-%{version}.css
cp -p css/%{altname}-responsive.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-responsive-%{version}.min.css
ln -s %{altname}-responsive-%{version}.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-responsive.src.css
ln -s %{altname}-responsive-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-responsive.css
ln -s %{altname}-responsive-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{altname}-responsive.min.css

cp -a img $RPM_BUILD_ROOT%{_appdir}

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
