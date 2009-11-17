#
Summary:	OpenStreetMap editor
Summary(pl.UTF-8):	Edytor OpenStreetMap
Name:		merkaartor
Version:	0.13.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://www.merkaartor.org/downloads/source/%{name}-%{version}.tar.bz2
# Source0-md5:	b3eccc1ccf1534a80258f5a24b13e661
URL:		http://www.merkaartor.org/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtScript-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Merkaartor is an openstreetmap mapping program. Merkaartor focuses on providing
a visually pleasing but performant editing environment for free geographical
data.

%prep
%setup -q
# you'll need this if you cp -a complete dir in source
# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
qmake-qt4 Merkaartor.pro \
	PREFIX="%{_prefix}"

%{__make} \
	CFLAGS='%{rpmcflags} -D_REENTRANT $(DEFINES)' \
	CXXFLAGS='%{rpmcxxflags} -D_REENTRANT $(DEFINES)' \
	LFLAGS="%{rpmldflags}" \

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%lang(es) %{_datadir}/%{name}/translations/merkaartor_es.ts
