Summary:	HFS volume utils 
Summary(pl):	Narzêdzia do woluminów HFS
Name:		hfsutils
Version:	3.2.6
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.mars.org/pub/hfs/%{name}-%{version}.tar.gz
Patch0:		%{name}.DESTDIR_1.patch
Patch1:		%{name}.DESTDIR_2.patch
Patch2:		%{name}.DESTDIR_3.patch
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
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf BLURB CREDITS INSTALL README ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
