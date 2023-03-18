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
Patch2:		%{name}-errno.patch
Patch3:		%{name}-include-c99.patch
Patch4:		%{name}-largefile.patch
URL:		http://www.mars.org/home/rob/proj/hfs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HFS volume utils.

%description -l pl.UTF-8
Narzędzia do woluminów HFS.

%package tcl
Summary:	Tcl based HFS utility shell
Summary(pl.UTF-8):	Powłoka narzędziowa HFS oparta na Tcl
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description tcl
Tcl based HFS utility shell.

%description tcl -l pl.UTF-8
Powłoka narzędziowa HFS oparta na Tcl.

%package tk
Summary:	Tk based HFS GUI
Summary(pl.UTF-8):	Oparty na Tk graficzny interfejs do HFS
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description tk
Tk based HFS GUI.

%description tk -l pl.UTF-8
Oparty na Tk graficzny interfejs do HFS.

%package devel
Summary:	Header files and static libraries for HFS
Summary(pl.UTF-8):	Pliki nagłówkowe i biblioteki statyczne do HFS
Group:		Development/Libraries

%description devel
Header files and static libraries for HFS.

%description devel -l pl.UTF-8
Pliki nagłówkowe i biblioteki statyczne do HFS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

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

CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64 -DUSE_INTERP_RESULT"
%configure \
	--enable-devlibs \
	--with-tcl \
	--with-tk
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BLURB CREDITS README CHANGES TODO doc/charset.txt
%attr(755,root,root) %{_bindir}/hattrib
%attr(755,root,root) %{_bindir}/hcd
%attr(755,root,root) %{_bindir}/hcopy
%attr(755,root,root) %{_bindir}/hdel
%attr(755,root,root) %{_bindir}/hdir
%attr(755,root,root) %{_bindir}/hformat
%attr(755,root,root) %{_bindir}/hfsutil
%attr(755,root,root) %{_bindir}/hls
%attr(755,root,root) %{_bindir}/hmkdir
%attr(755,root,root) %{_bindir}/hmount
%attr(755,root,root) %{_bindir}/hpwd
%attr(755,root,root) %{_bindir}/hrename
%attr(755,root,root) %{_bindir}/hrmdir
%attr(755,root,root) %{_bindir}/humount
%attr(755,root,root) %{_bindir}/hvol
%{_mandir}/man1/hattrib.1*
%{_mandir}/man1/hcd.1*
%{_mandir}/man1/hcopy.1*
%{_mandir}/man1/hdel.1*
%{_mandir}/man1/hdir.1*
%{_mandir}/man1/hformat.1*
%{_mandir}/man1/hfsutils.1*
%{_mandir}/man1/hls.1*
%{_mandir}/man1/hmkdir.1*
%{_mandir}/man1/hmount.1*
%{_mandir}/man1/hpwd.1*
%{_mandir}/man1/hrename.1*
%{_mandir}/man1/hrmdir.1*
%{_mandir}/man1/humount.1*
%{_mandir}/man1/hvol.1*

%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hfs
%attr(755,root,root) %{_bindir}/hfssh
%{_mandir}/man1/hfs.1*
%{_mandir}/man1/hfssh.1*

%files tk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xhfs
%{_mandir}/man1/xhfs.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libhfs.a
%{_libdir}/librsrc.a
%{_includedir}/hfs.h
%{_includedir}/rsrc.h
