# Generated by rust2rpm 24
%bcond_without check

Name:           chariott
Version:        main
Release:        %autorelease
Summary:        Chariott is a gRPC service that provides a common interface for interacting with applications.

License:        MIT
URL:            https://github.com/eclipse/chariott
Source:         https://github.com/eclipse/chariott/archive/main.tar.gz

BuildRequires:  rust-packaging >= 21
BuildRequires:  cmake
BuildRequires:  protobuf-devel
#BuildRequires:  protobuf # unsure if we still need
#BuildRequires:  protobuf-c-devel # unsure if we still need
BuildRequires:  rust-async-recursion+default-devel >= 1.0.0
BuildRequires:  rust-async-std+default-devel >= 1.12.0
BuildRequires:  rust-async-stream+default-devel >= 0.3.3
BuildRequires:  rust-async-trait+default-devel >= 0.1.0
BuildRequires:  rust-base64+default-devel >= 0.13.1
#BuildRequires:  bollard+default >= 0.13.0 # not found
BuildRequires:  rust-bytes+default-devel >= 1.2.0
BuildRequires:  rust-criterion+async_tokio-devel >= 0.4.0
BuildRequires:  rust-criterion+default-devel >= 0.4.0
BuildRequires:  rust-futures-util+default-devel >= 0.3.0
BuildRequires:  rust-futures+default-devel >= 0.3.0
BuildRequires:  rust-image+default-devel >= 0.24.4
#BuildRequires:  metrics-util+default >= 0.15.0 # not found
#BuildRequires:  ndarray+default >= 0.15.6 # not found
BuildRequires:  rust-prost-types+default-devel >= 0.11.0
BuildRequires:  rust-prost+default-devel >= 0.11.0
BuildRequires:  rust-rand+default-devel >= 0.8.0
BuildRequires:  rust-rand_distr+default-devel >= 0.4.0
BuildRequires:  rust-reqwest+default-devel >= 0.11.12
BuildRequires:  rust-reqwest+json-devel >= 0.11.12
#BuildRequires:  tensorflow+default >= 0.19.1 # not found
BuildRequires:  rust-test-case+default-devel >= 2.2.2
#BuildRequires:  test-log+default >= 0.2.10 # not found
BuildRequires:  rust-tokio-stream+default-devel >= 0.1.0
BuildRequires:  rust-tokio-stream+net-devel >= 0.1.0
BuildRequires:  rust-tokio-test+default-devel >= 0.4.2
BuildRequires:  rust-tokio-util+default-devel >= 0.7.3
BuildRequires:  rust-tokio+default-devel >= 1.21.2
BuildRequires:  rust-tokio+macros-devel >= 1.21.2
BuildRequires:  rust-tokio+rt-multi-thread-devel >= 1.21.2
BuildRequires:  rust-tokio+signal-devel >= 1.21.2
BuildRequires:  rust-tokio+sync-devel >= 1.21.2
BuildRequires:  rust-tokio+time-devel >= 1.21.2
#BuildRequires:  tonic-build+default >= 0.9.0 # not found
#BuildRequires:  tonic-reflection+default >= 0.9.0 # not found
#BuildRequires:  tonic+default >= 0.9.0 # not found
#BuildRequires:  tonic+transport >= 0.9.0 # not found
#BuildRequires:  tracing-subscriber+default >= 0.3.0 # not found
#BuildRequires:  tracing-subscriber+env-filter >= 0.3.0 # not found
BuildRequires:  rust-tracing+default-devel >= 0.1.0
BuildRequires:  rust-uuid+default-devel >= 1.2.1
BuildRequires:  rust-uuid+v4-devel >= 1.2.1

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n chariott-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
#%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license NOTICE
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%doc SECURITY.md
%{_bindir}/chariott
%{_bindir}/cloud-object-detection-app
%{_bindir}/dog-mode-logic-app
%{_bindir}/invoke-command
%{_bindir}/kv-app
%{_bindir}/local-object-detection-app
%{_bindir}/lt-consumer-app
%{_bindir}/lt-provider-app
%{_bindir}/mock-vas
%{_bindir}/simple-provider
%{_bindir}/simulated-camera-app

%changelog
%autochangelog
