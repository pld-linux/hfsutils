Summary:	HFS volume utils
Summary(pl):	Narzêdzia do woluminów HFS
Name:		hfsutils
Version:	3.2.6
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.mars.org/pub/hfs/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.mars.org/home/rob/proj/hfs/
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HFS volume utils.

%description -l pl
Narzêdzia do woluminów HFS.

%prep
%setup  -q
%patch0 -p1

%build
libtoolize --copy --force
aclocal
autoconf
autoheader

cd libhfs
aclocal 
autoconf
autoheader
cd ..

cd librsrc
aclocal
autoconf
autoheader
cd ..

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf BLURB CREDITS README CHANGES TODO doc/charset.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
