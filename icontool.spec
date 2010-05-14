%include	/usr/lib/rpm/macros.perl
Summary:	Icon Tools
Name:		icontool
Version:	0.1.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://launchpad.net/icontool/trunk/0.1/+download/%{name}-%{version}.tar.gz
# Source0-md5:	91fbba6fd0f518aa483a7ae8768e7469
URL:		https://launchpad.net/icontool
BuildRequires:	gawk
BuildRequires:	perl-base
BuildRequires:	perl-XML-Simple
BuildRequires:  rpm-perlprov >= 4.1-13
Requires:	inkscape
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A suite of tools for managing Icon Theme Specification and
Icon Naming Specification compliant icons in an application
or icon theme.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
