Summary:	HFS volume utils
Summary(pl):	Narz�dzia do wolumin�w HFS
Name:		hfsutils
Version:	3.2.6
Release:	2
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.mars.org/pub/hfs/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-ac.patch
URL:		http://www.mars.org/home/rob/proj/hfs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HFS volume utils.

%description -l pl
Narz�dzia do wolumin�w HFS.

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
