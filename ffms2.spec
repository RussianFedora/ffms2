Name:           ffms2
Version:        2.22
Release:        1%{?dist}
License:        MIT
Summary:        Wrapper library around libffmpeg
Url:            https://github.com/FFMS/ffms2/
Group:          System Environment/Libraries
Source0:        https://github.com/FFMS/%{name}/archive/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(zlib)

%description
FFmpegSource (usually known as FFMS or FFMS2) is a cross-platform wrapper
library around libffmpeg, plus some additional components to deal with file
formats libavformat has (or used to have) problems with.

%package devel
Summary:        Development package for ffms2
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:  pkgconfig
Requires:  pkgconfig(libavcodec)
Requires:  pkgconfig(libavformat)
Requires:  pkgconfig(libavutil)
Requires:  pkgconfig(libpostproc)
Requires:  pkgconfig(libswscale)
Requires:  pkgconfig(zlib)


%description devel
FFmpegSource (usually known as FFMS or FFMS2) is a cross-platform wrapper
library around libffmpeg, plus some additional components to deal with file
formats libavformat has (or used to have) problems with.

%prep
%setup -q -n %{name}-%{version}
sed -i 's/\r$//' COPYING

%build
#autoreconf -fi
%configure --disable-static --enable-shared
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/lib%{name}.la
rm -rf %{buildroot}%{_docdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING README.md
%{_bindir}/ffmsindex
%{_libdir}/lib%{name}.so.*

%files devel
%doc doc/*
%{_libdir}/lib%{name}.so
%{_includedir}/ffms*
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Nov 04 2015 Vasiliy N. Glazov <vascom2@gmail.com> 2.22-1.R
- Update to 2.22

* Sun Jun 28 2015 Ivan Epifanov <isage.dna@gmail.com> - 2.21-1.R
- Update to 2.21

* Mon Jan  5 2015 Ivan Epifanov <isage.dna@gmail.com> - 2.20-1.R
- Update to 2.20

* Fri Mar 28 2014 Ivan Epifanov <isage.dna@gmail.com> - 2.19-1.R
- Initial spec for Fedora
