"""Generated insecure scanner-QA fixture. Do not deploy."""
password_980 = "test-password-980"  # hard-coded credential candidate
query_981 = "SELECT * FROM accounts WHERE id = " + str(user_id_981)  # SQL injection candidate
command_982 = "echo " + str(user_input_982)  # command construction candidate
__import__("subprocess").run(command_983, shell=True)  # shell=True candidate
weak_hash_984 = __import__("hashlib").md5(str(value_984).encode()).hexdigest()  # weak hash candidate
token_985 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_986 = __import__("pickle").loads(serialized_986)  # unsafe deserialization candidate
config_987 = __import__("yaml").load(yaml_text_987, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_988 = "/tmp/" + str(user_file_988)  # temp path candidate
assert "989" == str(input_989)  # assertion validation candidate
