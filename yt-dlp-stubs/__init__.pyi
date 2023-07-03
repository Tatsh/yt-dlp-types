from typing import Any, Callable, Iterator, Literal, Mapping, NamedTuple, Sequence, TypedDict
import optparse

from typing_extensions import NotRequired

from .YoutubeDL import YoutubeDL

__all__ = ('YoutubeDL', 'parse_options')


class InfoDict(TypedDict):
    pass


class FormatContext(TypedDict):
    pass


class RetrySleepFunctions(TypedDict):
    default: NotRequired[Callable[[int], int]]
    file_access: NotRequired[Callable[[int], int]]
    fragment: NotRequired[Callable[[int], int]]


class ProgressTemplateValue(TypedDict):
    info: NotRequired[str]
    progress: NotRequired[str]


class ExternalDownloader(TypedDict):
    dash: NotRequired[str]
    default: NotRequired[str]
    ftp: NotRequired[str]
    http: NotRequired[str]
    m3u8: NotRequired[str]
    mms: NotRequired[str]
    rtmp: NotRequired[str]
    rtsp: NotRequired[str]


class DownloadRange(TypedDict):
    end_time: int
    index: NotRequired[int]
    start_time: int
    title: NotRequired[str]


class Color(TypedDict):
    stderr: NotRequired[Literal['always', 'auto', 'no_color', 'never']]
    stdout: NotRequired[Literal['always', 'auto', 'no_color', 'never']]


ProgressTemplate = TypedDict(
    'ProgressTemplate', {
        'download': ProgressTemplateValue,
        'download-title': ProgressTemplateValue,
        'postprocess': ProgressTemplateValue,
        'postprocess-title': ProgressTemplateValue
    })


class YDLOpts(TypedDict):
    #: Use netrc for authentication instead.
    usenetrc: bool | None
    #: Location of the netrc file. Defaults ``to ~/.netrc``.
    netrc_location: str | None
    #: Use a shell command to get credentials.
    netrc_cmd: str | None
    #: Username for authentication purposes.
    username: str | None
    #: Password for authentication purposes.
    password: str | None
    #: Two-factor authentication code
    twofactor: str | None
    #: Password for accessing a video.
    videopassword: str | None
    #: Adobe Pass multiple-system operator identifier.
    ap_mso: str | None
    #: Multiple-system operator account username.
    ap_username: str | None
    #: Multiple-system operator account password.
    ap_password: str | None
    #: Path to client certificate file in PEM format. May include the private key.
    client_certificate: str | None
    #: Path to private key file for client certificate.
    client_certificate_key: str | None
    #: Password for client certificate private key, if encrypted.
    client_certificate_password: str | None
    #: Do not print messages to stdout.
    quiet: bool | None
    #: Do not print out anything for warnings.
    no_warnings: bool | None
    #: Force printing final URL.
    #: Deprecated. Use ``forceprint``.
    forceurl: bool | None
    #: Force printing title.
    #: Deprecated. Use ``forceprint``.
    forcetitle: str | None
    #: Force printing ID.
    #: Deprecated. Use ``forceprint``.
    forceid: bool | None
    #: Force printing thumbnail URL.
    #: Deprecated. Use ``forceprint``.
    forcethumbnail: bool | None
    #: Force printing description.
    #: Deprecated. Use ``forceprint``.
    forcedescription: bool | None
    #: Force printing duration.
    #: Deprecated. Use ``forceprint``.
    forceduration: str | None
    #: Force printing final filename.
    #: Deprecated. Use ``forceprint``.
    forcefilename: bool | None
    #: A dict with keys WHEN mapped to a list of templates to print to stdout. The allowed keys are
    #: video or any of the items in ``utils.POSTPROCESS_WHEN``. For compatibility, a single list is
    #: also accepted.
    forceprint: Mapping[str, Sequence[str]] | Sequence[str] | None
    #: A dict with keys WHEN (same as forceprint) mapped to a list of tuples with
    #: (template, filename).
    print_to_file: Mapping[str, tuple[str, str]] | None
    #: Force printing ``info_dict`` as JSON.
    forcejson: bool | None
    #: Force printing the ``info_dict`` of the whole playlist (or video) as a single JSON line.
    dump_single_json: bool | None
    #: Force writing download archive regardless of ``skip_download`` or ``simulate``.
    force_write_download_archive: str | None
    #: Do not download the video files. If unset (or ``None``), simulate only if ``listsubtitles``,
    #: ``listformats`` or ``list_thumbnails`` is used.
    simulate: str | None
    #: Skip the actual download of the video file.
    skip_download: str | None
    #: Video format code. see "FORMAT SELECTION" for more details.
    #: You can also pass a function. The function takes 'ctx' as argument and returns the formats to
    #: download. See "build_format_selector" for an implementation
    format: str | Callable[[FormatContext], Mapping[str, Any]] | None
    #: Allow unplayable formats to be extracted and downloaded.
    allow_unplayable_formats: bool | None
    #: Ignore "No video formats" error. Useful for extracting metadata even if the video is not
    #: actually available for download (experimental).
    ignore_no_formats_error: bool | None
    #: A list of fields by which to sort the video formats. See "Sorting Formats" for more details.
    format_sort: Sequence[str] | None
    #: Force the given format_sort. see "Sorting Formats" for more details.
    format_sort_force: str | None
    #: Allow multiple video streams to be merged into a single file.
    allow_multiple_video_streams: bool | None
    #: Allow multiple audio streams to be merged into a single file.
    allow_multiple_audio_streams: bool | None
    #: Whether to test if the formats are downloadable. Can be ``True`` (check all), ``False`` (check
    #: none), ``'selected'`` (check selected formats), or ``None`` (check only if requested by
    #: extractor).
    check_formats: bool | Literal['selected'] | None
    #: Print an overview of available video formats and exit.
    listformats: bool | None
    #: Dictionary of templates for output names. Allowed keys are ``'default'`` and the keys of
    #: ``OUTTMPL_TYPES`` (in ``utils.py``). For compatibility with youtube-dl, a single string can
    #: also be used.
    outtmpl: str | Mapping[str, str] | None
    #: Placeholder for unavailable meta fields.
    outtmpl_na_placeholder: str | None
    #: Dictionary of output paths. The allowed keys are ``'home'``, ``'temp'``, and the keys of
    #: ``OUTTMPL_TYPES`` (in ``utils.py``).
    paths: str | None
    #: Do not allow ``'&'`` and spaces in file names.
    restrictfilenames: bool | None
    #: Force the filenames to be windows compatible.
    windowsfilenames: bool | None
    #: Do not stop on download/postprocessing errors. Can be ``'only_download'`` to ignore only
    #: download errors. Default is ``'only_download'`` for CLI, but ``False`` for API.
    ignoreerrors: bool | Literal['only_download'] | None
    #: Force downloader to use the generic extractor.
    #: Deprecated. Use ``allowed_extractors = ['generic', 'default']``.
    force_generic_extractor: bool | None
    #: List of regexes to match against extractor names that are allowed.
    allowed_extractors: Sequence[str] | None
    #: Download speed limit, in bytes/sec.
    ratelimit: int | None
    #: Assume the download is being throttled below this speed (bytes/sec).
    throttledratelimit: int | None
    #: Allow overwriting files.
    overwrites: bool | None
    #: Number of times to retry for expected network errors. Default is ``0`` for API, but ``10``
    #: for CLI.
    retries: int | None
    #: Number of times to retry on file access error (default: ``3``).
    file_access_retries: int | None
    #: Number of fragments of a dash/hlsnative video that should be downloaded concurrently.
    fragment_retries: int | None
    #: Number of times to retry for known errors (default: ``3``).
    extractor_retries: int | None
    #: Dictionary of functions that takes the number of attempts as argument and returns the time
    #: to sleep in seconds. Allowed keys are ``'http'``, ``'fragment'``, ``'file_access'``.
    retry_sleep_functions: RetrySleepFunctions | None
    #: Skip unavailable fragments for DASH, hlsnative and ISM downloads (default).
    skip_unavailable_fragments: bool | None
    #: Keep downloaded fragments on disk after downloading is finished
    keep_fragments: bool | None
    #: Number of fragments of a dash/hlsnative video that should be downloaded concurrently.
    concurrent_fragment_downloads: int | None
    #: Size of download buffer in bytes.
    buffersize: int | None
    #: Do not automatically resize the download buffer.
    noresizebuffer: bool | None
    #: Size of a chunk for chunk-based HTTP downloading. May be useful for bypassing bandwidth
    #: throttling imposed by a webserver (experimental).
    http_chunk_size: int | None
    #: Try to continue downloads if possible.
    continuedl: bool | None
    #: Do not print the progress bar.
    noprogress: bool | None
    #: Output progress bar as new lines.
    progress_with_newline: bool | None
    #: Dictionary of templates for progress outputs. Allowed keys are ``'download'``,
    #: ``'postprocess'``, ``'download-title'`` (console title) and ``'postprocess-title'``. The
    #: template is mapped on a dictionary with keys ``'progress'`` and ``'info'``.
    progress_template: ProgressTemplate | None
    #: Playlist item to start at.
    playliststart: int | None
    #: Playlist item to end at.
    playlistend: int | None
    #: Use ``playlist_items``. Download playlist items in reverse order.
    playlistreverse: bool | None
    #: Download playlist items in random order.
    playlistrandom: bool | None
    #: Process playlist entries as they are received.
    lazy_playlist: bool | None
    #: Download single video instead of a playlist if in doubt.
    noplaylist: bool | None
    #: Print everything to stderr instead of stdout.
    logtostderr: bool | None
    #: Display progress in console window's titlebar.
    consoletitle: str | None
    #: Do not use temporary ``.part`` files.
    nopart: bool | None
    #: Use the ``'Last-modified'`` header to set output file timestamps.
    updatetime: bool | None
    #: Write the video description to a ``.description`` file.
    writedescription: bool | None
    #: Write the video annotations to a ``.annotations.xml`` file.
    writeannotations: bool | None
    #: Write the video description to a ``.info.json`` file.
    writeinfojson: bool | None
    #: Whether to write playlists' description, ``info.json`` etc also to disk when using the
    #: ``'write*'`` options.
    allow_playlist_files: bool | None
    #: Remove internal metadata from the ``info.json``.
    clean_infojson: bool | None
    #: Extract video comments. This will not be written to disk unless ``writeinfojson`` is also
    #: given.
    getcomments: bool | None
    #: Write the thumbnail image to a file.
    writethumbnail: bool | None
    #: Write all thumbnail formats to files.
    write_all_thumbnails: bool | None
    #: Write an internet shortcut file, depending on the current platform
    #: (``.url``/``.webloc``/``.desktop``).
    writelink: bool | None
    #: Write a Windows internet shortcut file (``.url``).
    writeurllink: bool | None
    #: Write a macOS internet shortcut file (``.webloc``).
    writewebloclink: bool | None
    #:  Write a Linux internet shortcut file (``.desktop``).
    writedesktoplink: bool | None
    #: Write the video subtitles to a file.
    writesubtitles: bool | None
    #: Write the automatically generated subtitles to a file.
    writeautomaticsub: bool | None
    #: Use ``subtitleslangs = ['all']```. Downloads all the subtitles of the video (requires
    #: ``writesubtitles`` or ``writeautomaticsub``).
    allsubtitles: bool | None
    #: Lists all available subtitles for the video.
    listsubtitles: bool | None
    #: The format code for subtitles.
    subtitlesformat: str | None
    #: List of languages of the subtitles to download (can be regex). The list may contain
    #: ``"all"`` to refer to all the available subtitles. The language can be prefixed with a
    #: ``"-"`` to exclude it from the requested languages, e.g. ``['all', '-live_chat']``.
    subtitleslangs: Sequence[str] | None
    #: Download only matching titles.
    matchtitle: bool | None
    #: Reject downloads for matching titles.
    rejecttitle: bool | None
    #: Whether to prefer video formats with free containers over non-free ones of same quality.
    prefer_free_formats: bool | None
    #: Limit length of filename (extension excluded).
    trim_file_name: int | None
    #: Print additional info to stdout.
    verbose: bool | None
    #: Download only first bytes to test the downloader.
    test: bool | None
    #: Keep the video file after post-processing.
    keepvideo: str | None
    #: Skip files smaller than this size.
    min_filesize: int | None
    #: Skip files larger than this size.
    max_filesize: int | None
    #: An integer representing the minimum view count the video must have in order to not be
    #: skipped. Videos without view count information are always downloaded. ``None`` for no limit.
    min_views: str | None
    #: An integer representing the maximum view count the video must have in order to not be
    #: skipped. Videos without view count information are always downloaded. ``None`` for no limit.
    max_views: str | None
    #: A ``utils.DateRange`` object, download only if the upload_date is in the range.
    daterange: str | None
    #: Location of the cache files in the filesystem. ``False`` to disable filesystem cache.
    cachedir: str | None
    #: An integer representing the user's age in years. Unsuitable videos for the given age are
    #: skipped.
    age_limit: str | None
    #: A set, or the name of a file where all downloads are recorded. Videos already present in
    #: the file are not downloaded again.
    download_archive: str | None
    #: Stop the download process after attempting to download a file that is in the archive.
    break_on_existing: str | None
    #: Stop the download process when encountering a video that has been filtered out.
    #: Deprecated. Use `raise DownloadCancelled(msg)` in ``match_filter`` instead.
    break_on_reject: bool | None
    #: Whether ``break_on_reject`` and ``break_on_existing`` should act on each input URL as opposed
    #: to for the entire queue.
    break_per_url: bool | None
    #: Number of allowed failures until the rest of the playlist is skipped.
    skip_playlist_after_errors: bool | None
    #: File name or text stream from where cookies should be read and dumped to (Netscape format).
    cookiefile: str | None
    #: A tuple containing the name of the browser, the profile name/path from where cookies are
    #: loaded, the name of the keyring, and the container name, e.g. ``('chrome', )`` or
    #: ``('vivaldi', 'default', 'BASICTEXT')`` or ``('firefox', 'default', None, 'Meta')``.
    cookiesfrombrowser: tuple[str, ...] | None
    #: Explicitly allow HTTPS connection to servers that do not support RFC 5746 secure
    #: renegotiation.
    legacyserverconnect: bool | None
    #: Do not verify SSL certificates.
    nocheckcertificate: bool | None
    #: Use HTTP instead of HTTPS to retrieve information. Only supported by some extractors.
    prefer_insecure: str | None
    #: Enable ``file://`` URLs. This is disabled by default for security reasons.
    enable_file_urls: str | None
    #: A dictionary of custom headers to be used for all requests.
    http_headers: Mapping[str, str] | None
    #: URL of the proxy server to use.
    proxy: str | None
    #: Time to wait for unresponsive hosts, in seconds.
    socket_timeout: int | None
    #: Work around buggy terminals without bidirectional text support, using fridibi.
    bidi_workaround: bool | None
    #: Print out sent and received HTTP traffic
    debug_printtraffic: bool | None
    #: Deprecated.
    prefer_ffmpeg: bool | None
    #: Download ads as well (does not work).
    include_ads: bool | None
    #: Prepend this string if an input url is not valid. ``'auto'`` for elaborate guessing.
    default_search: str | None
    #: Whether to process dynamic DASH manifests (default: ``True``).
    dynamic_mpd: bool | None
    #: A dictionary of arguments to be passed to the extractors. See "EXTRACTOR ARGUMENTS" for
    #: details. Example: ``{'youtube': {'skip': ['dash', 'hls']}}``.
    extractor_args: Mapping[str, Mapping[str, Any]] | None
    #: Use ``extractor_args``. If ``True`` (default), DASH manifests and related data will be
    #: downloaded and processed by extractor. You can reduce network I/O by disabling it if you don't
    #: care about DASH. Only for YouTube.
    youtube_include_dash_manifest: bool | None
    #: Use ``extractor_args``. If ``True`` (default), DASH manifests and related data will be
    #: downloaded and processed by extractor. You can reduce network I/O by disabling it if you don't
    #: care about HLS. Only for YouTube.
    youtube_include_hls_manifest: bool | None
    #: Use this encoding instead of the system-specified.
    encoding: str | None
    #: Whether to resolve and process ``url_results`` further.
    #: * ``False``: Always process. Default for API.
    #: * ``True``: Never process.
    #: * ``'in_playlist'``: Do not process inside playlist/multi-video.
    #: * ``'discard'``: Always process, but don't return the result from inside playlist/multi-video.
    #: * ``'discard_in_playlist'``: Same as ``'discard'``, but only for playlists (not multi_video).
    #:   Default for CLI.
    extract_flat: bool | Literal['in_playlist', 'discard', 'discard_in_playlist'] | None
    #: Whether to download livestreams videos from the start.
    live_from_start: bool | None
    #: If given, wait for scheduled streams to become available. The value should be a tuple
    #: containing the range (min_secs, max_secs) to wait between retries.
    wait_for_video: tuple[int, int] | None
    #: Mark videos watched (even with ``--simulate``). Only for YouTube.
    mark_watched: bool | None
    #: ``"/"`` separated list of extensions to use when merging formats.
    merge_output_format: str | None
    #: Expected final extension; used to detect when the file was already downloaded and
    #: converted.
    final_ext: str | None
    #: A list of dictionaries, each with an entry
    #: * key:  The name of the postprocessor. See ``yt_dlp/postprocessor/__init__.py`` for a list.
    #: * when: When to run the postprocessor. Allowed values are the entries of
    #: ``utils.POSTPROCESS_WHEN``. Assumed to be ``'post_process'`` if not given.
    postprocessors: dict[str,
                         Literal['pre_process', 'after_filter', 'video', 'before_dl',
                                 'post_process', 'after_move', 'after_video', 'playlist']] | None
    #: Automatically correct known faults of the file.
    #: One of:
    #: - ``"never"``: do nothing
    #: - ``"warn"``: only emit a warning
    #: - ``"detect_or_warn"``: check whether we can do anything about it, warn otherwise (default)
    fixup: Literal['never', 'warn', 'detect_or_warn'] | None
    #: Client-side IP address to bind to.
    source_address: str | None
    #: ``True`` if we are allowed to contact the yt-dlp servers for debugging. Not implemented.
    call_home: bool | None
    #: Number of seconds to sleep between requests .during extraction
    sleep_interval_requests: int | None
    #: Number of seconds to sleep before each download when used alone or a lower bound of a
    #: range for randomized sleep before each download (minimum possible number of seconds to
    #: sleep) when used along with ``max_sleep_interval``.
    sleep_interval: int | None
    #: Upper bound of a range for randomized sleep before each download (maximum possible number
    #: of seconds to sleep). Must only be used along with sleep_interval. Actual sleep time will
    #: be a random float from range ``[sleep_interval; max_sleep_interval]``.
    max_sleep_interval: int | None
    #: Number of seconds to sleep before each subtitle download.
    sleep_interval_subtitles: int | None
    #: A dictionary of protocol keys and the executable of the external downloader to use for it.
    #: Set the value to ``'native'`` to use the native downloader.
    external_downloader: ExternalDownloader | None
    #: A callback function that gets called for every video with the signature
    #:  ``(info_dict, ydl) -> Iterable[Section]``. Only the returned sections will be downloaded.
    #:  Each Section is a dict with the following keys:
    #: * start_time: Start time of the section in seconds
    #: * end_time: End time of the section in seconds
    #: * title: Section title (Optional)
    #: * index: Section number (Optional)
    download_ranges: Callable[[Any, YoutubeDL], Iterator[DownloadRange]] | None
    #: Re-encode the video when downloading ranges to get precise cuts
    force_keyframes_at_cuts: bool | None
    #: Print a table of all thumbnails and exit.
    list_thumbnails: str | None
    #: Specific indices of playlist to download.
    playlist_items: Sequence[int] | None
    #: Set ``ytdl.filesize`` user xattribute with expected size.
    xattr_set_filesize: bool | None
    #: A function that gets called for every video with the signature
    #: ``(info_dict, *, incomplete: bool) -> str | None``
    #: For backward compatibility with youtube-dl, the signature
    #: ``(info_dict) -> str | None`` is also allowed.
    #: If it returns a message, the video is ignored.
    #: If it returns ``None``, the video is downloaded.
    #: If it returns utils.NO_DEFAULT, the user is interactively asked whether to download the video.
    #: Raise ``utils.DownloadCancelled(msg)`` to abort remaining downloads when a video is rejected.
    #: ``match_filter_func`` in utils.py is one example for this.
    match_filter: Callable[[InfoDict, bool], str | None] | Callable[[InfoDict], str | None] | None
    #: A Dictionary with output stream names as keys and their respective color policy as values.
    #: Can also just be a single color policy, in which case it applies to all outputs.
    #: Valid stream names are ``'stdout'`` and ``'stderr'``. Valid color policies are one of
    #: ``'always'``, ``'auto'``, ``'no_color'``, or ``'never'``.
    color: Color | None
    #: Location of the ffmpeg binary; either the path to the binary or its containing directory.
    ffmpeg_location: str | None
    #: Use ``external_downloader = {'m3u8': 'native'}`` or ``{'m3u8': 'ffmpeg'}``.
    #: Use the native HLS downloader instead of ffmpeg.
    hls_prefer_native: bool | None
    #: Use the mpegts container for HLS videos.
    hls_use_mpegts: bool | None
    #: Split HLS playlists to different formats at discontinuities such as ad breaks (default:
    #: ``False``).
    hls_split_discontinuity: bool | None
    #: Abort after downloading NUMBER files.
    max_downloads: int | None
    #: Print downloaded pages encoded using base64 to debug problems (very verbose)
    dump_intermediate_pages: bool | None
    #: List formats as a table.
    listformats_table: bool | None
    #: Write downloaded intermediary pages to files in the current directory to debug problems.
    write_pages: bool | None
    #: A dictionary of downloader keys (in lower case) and a list of additional command-line
    #: arguments for the executable. Use ``'default'`` as the name for arguments to be passed to all
    #: downloaders. For compatibility with youtube-dl, a single list of args can also be used.
    external_downloader_args: Literal['default'] | Mapping[str,
                                                           Sequence[str]] | Sequence[str] | None
    #: A dictionary of postprocessor/executable keys (in lower case) and a list of additional
    #: command-line arguments for the postprocessor/executable. The dict can also have "PP+EXE" keys
    #: which are used when the given exe is used by the given PP. Use ``'default'`` as the name for
    #: arguments to passed to all PP. For compatibility with youtube-dl, a single list of args can
    #: also be used.
    postprocessor_args: Mapping[str, Sequence[str]] | Sequence[str] | None
    #: URL of the proxy to use for IP address verification on geo-restricted sites.
    geo_verification_proxy: str | None
    #: Bypass geographic restriction via faking X-Forwarded-For HTTP header
    geo_bypass: bool | None
    #: Two-letter ISO 3166-2 country code that will be used for explicit geographic restriction
    #: bypassing via faking X-Forwarded-For HTTP header.
    geo_bypass_country: str | None
    #: IP range in CIDR notation that will be used similarly to ``geo_bypass_country``.
    geo_bypass_ip_block: str | None
    #: Compatibility options. See "Differences in default behavior". The following options do not
    #: work when used through the API: filename, abort-on-error, multistreams, no-live-chat,
    #: format-sort, no-clean-infojson, no-playlist-metafiles, no-keep-subs, no-attach-info-json.
    #: Refer ``__init__.py`` for their implementation
    compat_opts: dict[str, Any] | None
    # Undocumented fields below.
    _deprecation_warnings: Sequence[str] | None
    _warnings: Sequence[str] | None
    autonumber_size: int | None
    autonumber_start: int | None
    cn_verification_proxy: str | None
    #: Does nothing.
    forceformat: Any
    load_pages: bool | None
    youtube_print_sig_code: bool | None


class ParsedOptions(NamedTuple):
    parser: Any
    options: optparse.Values
    urls: Sequence[str]
    ydl_opts: YDLOpts


def parse_options(argv: Sequence[str] | None = ...) -> ParsedOptions:
    ...
