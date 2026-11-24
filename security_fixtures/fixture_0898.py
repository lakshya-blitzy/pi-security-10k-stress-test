"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8980 = "test-password-8980"  # hard-coded credential candidate
query_8981 = "SELECT * FROM accounts WHERE id = " + str(user_id_8981)  # SQL injection candidate
command_8982 = "echo " + str(user_input_8982)  # command construction candidate
__import__("subprocess").run(command_8983, shell=True)  # shell=True candidate
weak_hash_8984 = __import__("hashlib").md5(str(value_8984).encode()).hexdigest()  # weak hash candidate
token_8985 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8986 = __import__("pickle").loads(serialized_8986)  # unsafe deserialization candidate
config_8987 = __import__("yaml").load(yaml_text_8987, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8988 = "/tmp/" + str(user_file_8988)  # temp path candidate
assert "8989" == str(input_8989)  # assertion validation candidate
