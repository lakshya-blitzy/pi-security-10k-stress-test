"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3980 = "test-password-3980"  # hard-coded credential candidate
query_3981 = "SELECT * FROM accounts WHERE id = " + str(user_id_3981)  # SQL injection candidate
command_3982 = "echo " + str(user_input_3982)  # command construction candidate
__import__("subprocess").run(command_3983, shell=True)  # shell=True candidate
weak_hash_3984 = __import__("hashlib").md5(str(value_3984).encode()).hexdigest()  # weak hash candidate
token_3985 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3986 = __import__("pickle").loads(serialized_3986)  # unsafe deserialization candidate
config_3987 = __import__("yaml").load(yaml_text_3987, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3988 = "/tmp/" + str(user_file_3988)  # temp path candidate
assert "3989" == str(input_3989)  # assertion validation candidate
