%global major 1
%define libname %mklibname nvidia-egl-wayland %major
%define devname %mklibname -d nvidia-egl-wayland
%global commit  6f5f7d0d50287b810e9dec4718d3cf995fed809a
%global date 20180201
%global shortcommit0 %(c=%{commit}; echo ${c:0:7})

Name:		egl-wayland
Version:	1.0.3
Release:	1
Group:		System/Libraries
Summary:	Wayland EGL External Platform library
License:	MIT
URL:		https://github.com/NVIDIA
Source0:	%url/%{name}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
Source1:	10_nvidia_wayland.json
BuildRequires:	meson
BuildRequires:	libtool
BuildRequires:	eglexternalplatform-devel
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(GL)
BuildRequires:	pkgconfig(wayland)

# Required for directory ownership
Requires:	libglvnd-egl%{?_isa}

%description
%summary.

%package -n %{libname}
Summary:	%summary
Group:		System/Libraries

%description -n %{libname}
%summary.

%package -n %{devname}
Summary:	Wayland EGL External Platform library development package
Group:		Development/C
Requires:	%{libname}%{?_isa} = %{EVRD}

%description -n %{devname}
Wayland EGL External Platform library development package.

%prep
%autosetup -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install
install -m 0755 -d %{buildroot}%{_datadir}/egl/egl_external_platform.d/
install -pm 0644 %{SOURCE1} %{buildroot}%{_datadir}/egl/egl_external_platform.d/
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files -n %libname
%doc README.md
%license COPYING
%{_libdir}/*.so.*
%{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json

%files -n %devname
%{_libdir}/libnvidia-egl-wayland.so
%{_datadir}/pkgconfig/wayland-eglstream.pc
%{_datadir}/pkgconfig/wayland-eglstream-protocols.pc
%{_datadir}/wayland-eglstream/
