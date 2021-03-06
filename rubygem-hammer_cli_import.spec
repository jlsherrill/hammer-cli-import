%global gemname hammer_cli_import
%global confdir hammer
%if 0%{?rhel}
%global gem_dir /usr/lib/ruby/gems/1.8
%endif
%if 0%{?rhel} > 6
%global gem_dir /usr/share/gems
%endif


%global geminstdir %{gem_dir}/gems/%{gemname}-%{version}

Name:       rubygem-%{gemname}
Version:    0.10.1
Release:    1%{?dist}
Summary:    Sat5-import command plugin for the Hammer CLI

Group:      Development/Languages
License:    GPLv3
URL:        https://github.com/Katello/hammer-cli-import
Source0:    %{gemname}-%{version}.gem
Source1:    import.yml
Source2:    role_map.yml
Source3:    config_macros.yml
Source4:    interview_answers.yml

%if 0%{?rhel} > 6 || 0%{?fedora} > 18
Requires: ruby(release)
%else
Requires: ruby(abi)
%endif
Requires: ruby(rubygems)
Requires: rubygem(hammer_cli)
BuildRequires: ruby(rubygems)
%if 0%{?fedora}
BuildRequires: rubygems-devel
%endif
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Sat5-import plugin for the Hammer CLI

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d/import
install -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d/import.yml
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d/import/role_map.yml
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d/import/config_macros.yml
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d/import/interview_answers.yml
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{geminstdir}
%{geminstdir}/
%config(noreplace) %{_sysconfdir}/%{confdir}/cli.modules.d/import.yml
%config(noreplace) %{_sysconfdir}/%{confdir}/cli.modules.d/import/role_map.yml
%config(noreplace) %{_sysconfdir}/%{confdir}/cli.modules.d/import/config_macros.yml
%config(noreplace) %{_sysconfdir}/%{confdir}/cli.modules.d/import/interview_answers.yml
%exclude %{gem_dir}/cache/%{gemname}-%{version}.gem
%{gem_dir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gemname}-%{version}

%changelog
* Tue Aug 19 2014 Tomas Lestach <tlestach@redhat.com> 0.10.1-1
- fix content host and host collection association (tlestach@redhat.com)
- enhance exception message (tlestach@redhat.com)
- use set instead of an array (tlestach@redhat.com)
- generate 1 server rpm instead of client rpm per org (tlestach@redhat.com)
- 1130183 - Use extends (so needed methods will be added) (mkollar@redhat.com)
- Use existing logging capabilities (mkollar@redhat.com)
- 1130183 - Add possibility to things in one thread (mkollar@redhat.com)
- Typo (mkollar@redhat.com)
- 1130508 - add --delete to 'all' (ggainey@redhat.com)
- 1127800 - let's work with uuid as content host id (tlestach@redhat.com)
- 1120839 - Backtrace log level finetuning (mkollar@redhat.com)
- replace all underscore characters with spaces (tlestach@redhat.com)
- Handle MissingObjectError in appropriate way (mkollar@redhat.com)
- allow deleting content views without any versions published
  (tlestach@redhat.com)
- enhance to_singular method (tlestach@redhat.com)
- replace all unallowed characters from content view names
  (tlestach@redhat.com)
- add one more sytem profile to simple test (tlestach@redhat.com)
- 1125035 - Removed some more no-longer-relevant TODO comments
  (ggainey@redhat.com)
- 1125035 - Remove ancient TODO comment, because it was to-did
  (ggainey@redhat.com)
- Associate ak with environment (mkollar@redhat.com)
- Enhance readme (mkollar@redhat.com)

* Mon Aug 11 2014 Grant Gainey 0.10.0-1
- allow content view --delete to be executed multiple times
  (tlestach@redhat.com)
- move initialization of @map earlier (tlestach@redhat.com)
- introduce --delete option for simple test (tlestach@redhat.com)
- Rubocop doesn't like some of out more-complicated things.
  (ggainey@redhat.com)
- Fix our attempt to publish RH-content-view. Spit out a useful error when it
  fails (ggainey@redhat.com)
- do not delete orgs, since it's disabled (tlestach@redhat.com)
- introduce post_delete (tlestach@redhat.com)
- include persistent map (tlestach@redhat.com)
- add content-host import to the simple test (tlestach@redhat.com)
- system_content_views persistant map (tlestach@redhat.com)
- sort persistent maps alphabetically (tlestach@redhat.com)
- associate content views with content hosts (tlestach@redhat.com)
- check among redhat content view, if id not found among the custom content
  views (tlestach@redhat.com)
- start creating composite content views for content hosts
  (tlestach@redhat.com)
- let's use Spacewalk 2.2 client as 2nd repository (tlestach@redhat.com)
- fix bracket for better substitution (tlestach@redhat.com)
- add activation keys to simple test (tlestach@redhat.com)
- move composite content view creation to importtools (tlestach@redhat.com)
- Skip activation-keys with 'Satellite default' (mkollar@redhat.com)
- 1126239 - Add content-host to Things Import-All Knows (ggainey@redhat.com)
- 1126882 - move default-cfgs to cli.modules.d/import (ggainey@redhat.com)
- 1127263 - Add info about files and puppet-modules to summary
  (ggainey@redhat.com)
- 1126618 - false != :false, was causing upload to *always* be skipped
  (ggainey@redhat.com)
- Use preferred way to map existing entities (mkollar@redhat.com)
- 1126155 - slightly better (mkollar@redhat.com)
- 1126155 - hide potentially confusing messages (mkollar@redhat.com)
- --export-directory option not required with combination of --delete option
  (tlestach@redhat.com)
- No really, fixing args for import-all for *sure* this time
  (ggainey@redhat.com)
- Fix arg-breakage in import-all (ggainey@redhat.com)
- Be consistent in plural for report_summary (mkollar@redhat.com)
- 1126618 - Add --generate-only to config-file (ggainey@redhat.com)
- Report sipping of content-view (mkollar@redhat.com)
- 1126842 - Need to quote the values in config_macros.yml (ggainey@redhat.com)
- Fix logging so that --debug actually works (ggainey@redhat.com)
- 1126493 - Set 'description' for cfg-chan puppet module. Fix it so
  #{module_name} actually works as well (ggainey@redhat.com)
- 1126027 - create product/repo for local stuff only when needed
  (mkollar@redhat.com)
- Handle empty summary nicely (mkollar@redhat.com)
- configfile - hide unsilence-able puppet output (ggainey@redhat.com)

* Sun Aug 03 2014 Grant Gainey 0.9.1-1
- Minor comment cleanup (ggainey@redhat.com)
- Rubocop: Prefer single-quoted strings when you don't need string
  interpolation or special symbols. (ggainey@redhat.com)
- Don't override execute just to do something once (ggainey@redhat.com)
- 1126103 - config-file needs its own persistence-type, :puppet_repositories
  (ggainey@redhat.com)
- Add correct missing interview_answers.yml (ggainey@redhat.com)
- missing interview_answers.yml prevents RPM from building (lpramuk@redhat.com)
- 1126063 - Teach import config-file to find/use interview_answers.yml
  (ggainey@redhat.com)
- Report repository skipping (mkollar@redhat.com)
- Report manifest uploading (mkollar@redhat.com)
- Summary reporting (mkollar@redhat.com)
- add another repo to the test (tlestach@redhat.com)
- update sync repo message (tlestach@redhat.com)
- work with absolute path (tlestach@redhat.com)
- create simple content views within the test (tlestach@redhat.com)
- do not count the entities in the test (tlestach@redhat.com)
- print the issued import command (tlestach@redhat.com)
- run the tests in verbose mode (tlestach@redhat.com)
- just notify about unexpected entity count instead of dying
  (tlestach@redhat.com)
- change tests org_id to 100 (tlestach@redhat.com)
- enhance test (tlestach@redhat.com)
- Rubocop: lib/hammer_cli_import/user.rb:85:77: C: Do not use semicolons to
  terminate expressions. lib/hammer_cli_import/all.rb:135:7: C: Cyclomatic
  complexity for build_args is too high. [12/11] (ggainey@redhat.com)
- 1124967 - teach upload-manifest to wait for task to finish
  (ggainey@redhat.com)
- 1125034 - teach --verbose to only emit if >= current-log-level
  (ggainey@redhat.com)
- 1125266 - Turn on using Sat6-API to get role-list (ggainey@redhat.com)
- configfile - add macro-mapping to RPM (ggainey@redhat.com)
- configfile - add to 'all' command (ggainey@redhat.com)
- configfiles - Everything works now (including --delete) (ggainey@redhat.com)
- create rpmbuild structure (tlestach@redhat.com)
- export system-id_to_uuid files (tlestach@redhat.com)
- enhance debug message (tlestach@redhat.com)
- fix content host deletion (tlestach@redhat.com)
- content host change (tlestach@redhat.com)
- change type (tlestach@redhat.com)
- Rubocop: Style/Blocks (mkollar@redhat.com)
- Rubocop: Style/LineLength (mkollar@redhat.com)
- Rubocop: Style/PerlBackrefs (mkollar@redhat.com)
- Rubocop: Style/NegatedWhile (mkollar@redhat.com)
- Rubocop: Style/MethodCallParentheses (mkollar@redhat.com)
- Rubocop: Style/EmptyLinesAroundBody (mkollar@redhat.com)
- Rubocop: Style/WhileUntilDo (mkollar@redhat.com)
- Rubocop: Style/SpaceInsideParens (mkollar@redhat.com)
- Rubocop: Style/DeprecatedHashMethods (mkollar@redhat.com)
- Rubocop: Lint/UnusedMethodArgument (mkollar@redhat.com)
- Rubocop: Lint/UnusedBlockArgument (mkollar@redhat.com)
- Rubocop: Style/StringLiterals (mkollar@redhat.com)
- configfiles - DRAFT, main path generally working (ggainey@redhat.com)

* Mon Jul 28 2014 Grant Gainey 0.9.0-1
- 1123837 - Allow hosts with no dot (only tld) (mkollar@redhat.com)
- Check CSV file headers sooner (mkollar@redhat.com)
- 1121131 - Add reportname attr to commands to describe which sw-report they
  understand (ggainey@redhat.com)
- 1122169 - Add someexplanantion to --upload-manifests-from
  (ggainey@redhat.com)
- 1121986 - setup logging at init, not at execute (ggainey@redhat.com)
- Do not discard content of log file (prefer append) (mkollar@redhat.com)
- Activation keys with contentviews with rh cotent (mkollar@redhat.com)
- sat6-latest appears to no longer wrap orgs (ggainey@redhat.com)
- Add support for clones of Red Hat Channels (mkollar@redhat.com)
- Do not mix translated and untranslated ids (mkollar@redhat.com)

* Tue Jul 15 2014 Grant Gainey 0.8.0-1
- rubocop, where is thy sting? (ggainey@redhat.com)
- Sprint-7 demo response: standardize logging * Added calls for
  debug/info/progress/wanbr/error/fatal * Added quiet/verbose/debug/logfile
  switches * Changed instances of 'puts' and 'p' to use the new options
  (ggainey@redhat.com)
- Fiddle with asyntaskscreactor statuses... (mkollar@redhat.com)
- Use ID instead of label (mkollar@redhat.com)
- More suitable message (mkollar@redhat.com)
- Protect persistent map (mkollar@redhat.com)
- Teach all about wait/sync (ggainey@redhat.com)
- Teach 'all' about manifest-directory (ggainey@redhat.com)
- fixed: WARN Legacy configuration of modules detected. (lpramuk@redhat.com)
- specfile: on rhel7 gems live elsewhere (lpramuk@redhat.com)
- O(n log n) -> O(n) (mkollar@redhat.com)
- Removing debugging-rescue (ggainey@redhat.com)
- RuboCop (mkollar@redhat.com)
- Last synced field might not be parsable (mkollar@redhat.com)
- Look for and upload manifests as we import organizations (ggainey@redhat.com)
- Integrate reactor into repository-enable (mkollar@redhat.com)
- Just a little note for the future generations (mkollar@redhat.com)
- Handle non-mapped channels (mkollar@redhat.com)
- Move check for existence of file to the right place (mkollar@redhat.com)
- Fix capitalization (mkollar@redhat.com)
- Better debugging message (mkollar@redhat.com)
- Consistency (mkollar@redhat.com)
- One TODO down... (mkollar@redhat.com)
- Detect sync in progress (mkollar@redhat.com)
- Allow user to do Ctrl-C (mkollar@redhat.com)
- Update README (mkollar@redhat.com)
- RuboCop ... almost (mkollar@redhat.com)
- Fix me! 87 (mkollar@redhat.com)
- Be more specific about exception caught (mkollar@redhat.com)
- Whoops... (mkollar@redhat.com)
- Unnecessary proc re-creaction (mkollar@redhat.com)
- Check whether we are deleting compatible entity (mkollar@redhat.com)
- RuboCop: SignalException (mkollar@redhat.com)
- Make raising/failing consistent (mkollar@redhat.com)
- Run tasks with no prerequisites in main thread (mkollar@redhat.com)
- Cleanup (mkollar@redhat.com)
- move content view deletion to a separate module, so we can re-use it from
  multiple subcommands (tlestach@redhat.com)
- create a common composite_rhcv_id (tlestach@redhat.com)
- delete Red Hat content views (tlestach@redhat.com)
- some repos do not have 'url' (tlestach@redhat.com)
- create content views from Red Hat channels (tlestach@redhat.com)
- Use new repository synchronization (mkollar@redhat.com)
- New methods for repository syncing (mkollar@redhat.com)
- Be more verbose when main thread finished (mkollar@redhat.com)
- Catch exceptions in asynchronous tasks... (mkollar@redhat.com)
- Start using AsyncTasksReactor (mkollar@redhat.com)
- Determine state of multiple asynchronous tasks (mkollar@redhat.com)
- Meanwhile in the real world... (mkollar@redhat.com)
- Alternate status messages (mkollar@redhat.com)
- AsyncTasksReactor playground (mkollar@redhat.com)
- Reactor for asynchronous tasks (mkollar@redhat.com)
- move read_channel_map to a separate file in 'scripts' directory
  (tlestach@redhat.com)
- enhance error message (tlestach@redhat.com)
- sort persistent map definitions (tlestach@redhat.com)
- sat6 system uuid is actually a String ... (tlestach@redhat.com)
- associate virtual guests for virtual hosts (tlestach@redhat.com)
- introduce migrating of system profiles to content hosts (tlestach@redhat.com)
- We can iterate over users directly (mkollar@redhat.com)
- fix commas (tlestach@redhat.com)
- more universal transcript (tlestach@redhat.com)
- sort the @prerequisite keys (tlestach@redhat.com)
- inserting one key=>value into a hash multiple times does not make any
  difference (tlestach@redhat.com)
- RuboCop (mkollar@redhat.com)
- Avoid problems in the future (mkollar@redhat.com)
- Avoid problems (mkollar@redhat.com)
- Describe args using args.join() instead of args.inspect (ggainey@redhat.com)
- Teach 'all' about new entities and new options (ggainey@redhat.com)
- 1114103 - Don't assume @prereqs quite so much (ggainey@redhat.com)
- Method api_init actually can be called multiple times (mkollar@redhat.com)
- :users needs :orgs as prereq (ggainey@redhat.com)
- organization simplification (tlestach@redhat.com)
- extend cache search and detect already enabled/unknown repos
  (tlestach@redhat.com)
- store repo to cache (tlestach@redhat.com)
- allow to disable repository_sets (tlestach@redhat.com)
- introduce prerequisities for server entities (tlestach@redhat.com)
- map redhat repositories (tlestach@redhat.com)
- move per row work to import_single_row (tlestach@redhat.com)
- Reproducers HOW TO (mkollar@redhat.com)
- rubocop-0.24.0 issue (tlestach@redhat.com)
- Revert back to get_cache so we only enable repos for orgs that the tool knows
  about. Add some messaging to avoid user-confusion. (ggainey@redhat.com)
- Nicer message (mkollar@redhat.com)

* Tue Jun 24 2014 Grant Gainey 0.7.2-1
- Subcommand and option name-chgs in response to comments (ggainey@redhat.com)

* Mon Jun 23 2014 Grant Gainey 0.7.1-1
- Update to 0.7.0 (ggainey@redhat.com)

* Mon Jun 23 2014 Grant Gainey 0.6.2-1
- Add some more documentation (mkollar@redhat.com)
- Some sanity checking (mkollar@redhat.com)
- Added some documentation (mkollar@redhat.com)
- let's build rubygem-hammer_cli_import to katello-nightly-rhel6 tag
  (tlestach@redhat.com)

* Thu Jun 19 2014 Grant Gainey 0.6.1-1
- * Look for the default repository-map where the gem puts it * Clarify the
  output when we decide to enable a repo (ggainey@redhat.com)
- let git ignore .swp files (tlestach@redhat.com)

* Thu Jun 19 2014 Tomas Lestach <tlestach@redhat.com> 0.6.0-1
- initial hammer-cli-import tag


