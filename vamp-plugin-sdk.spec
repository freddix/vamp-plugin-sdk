Summary:	API for audio analysis and feature extraction plugins
Name:		vamp-plugin-sdk
Version:	2.4
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://code.soundsoftware.ac.uk/attachments/download/517/%{name}-%{version}.tar.gz
# Source0-md5:	4bd75ca4515c141cd8776bdb59066261
Patch:		%{name}-link.patch
URL:		http://www.vamp-plugins.org/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vamp is an audio processing plugin system for plugins that extract
descriptive information from audio data - typically referred to as
audio analysis plugins or audio feature extraction plugins.

%package devel
Summary:	Header files for vamp library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for vamp library.

%package examples
Summary:	Example vamp plugins
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description examples
Example vamp plugins.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make} \
	CXX="%{__cxx}"	\
	LDFLAGS="%{rpmldflags} %{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT			\
	INSTALL_PKGCONFIG="%{_pkgconfigdir}"	\
	INSTALL_PLUGINS="%{vampplugindir}"	\
	INSTALL_SDK_LIBS="%{_libdir}"

install -d $RPM_BUILD_ROOT%{_libdir}/vamp
install examples/*.so $RPM_BUILD_ROOT%{_libdir}/vamp

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%dir %{_libdir}/vamp
%attr(755,root,root) %{_bindir}/vamp-rdf-template-generator
%attr(755,root,root) %ghost %{_libdir}/libvamp-hostsdk.so.?
%attr(755,root,root) %ghost %{_libdir}/libvamp-sdk.so.?
%attr(755,root,root) %{_libdir}/libvamp-hostsdk.so.*.*.*
%attr(755,root,root) %{_libdir}/libvamp-sdk.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvamp-hostsdk.so
%attr(755,root,root) %{_libdir}/libvamp-sdk.so
%{_libdir}/libvamp-hostsdk.la
%{_libdir}/libvamp-sdk.la
%{_includedir}/vamp
%{_includedir}/vamp-sdk
%{_includedir}/vamp-hostsdk
%{_pkgconfigdir}/*.pc

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vamp-simple-host
%attr(755,root,root) %{_libdir}/vamp/*so

