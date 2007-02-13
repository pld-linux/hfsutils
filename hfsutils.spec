# TODO
# - move progs to sbindir like other mkfs tools
Summary:	HFS volume utils
Summary(pl.UTF-8):	Narzędzia do woluminów HFS
Name:		hfsutils
Version:	3.2.6
Release:	3
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.mars.org/pub/hfs/%{name}-%{version}.tar.gz
# Source0-md5:	fa572afd6da969e25c1455f728750ec4
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-ac.patch
URL:		http://www.mars.org/home/rob/proj/hfs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HFS volume utils.

%description -l pl.UTF-8
Narzędzia do woluminów HFS.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}

cd libhfs
%{__aclocal}
%{__autoconf}
%{__autoheader}
cd ..

cd librsrc
%{__aclocal}
%{__autoconf}
%{__autoheader}
cd ..

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BLURB CREDITS README CHANGES TODO doc/charset.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
