"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7980 = "test-password-7980"  # hard-coded credential candidate
query_7981 = "SELECT * FROM accounts WHERE id = " + str(user_id_7981)  # SQL injection candidate
command_7982 = "echo " + str(user_input_7982)  # command construction candidate
__import__("subprocess").run(command_7983, shell=True)  # shell=True candidate
weak_hash_7984 = __import__("hashlib").md5(str(value_7984).encode()).hexdigest()  # weak hash candidate
token_7985 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7986 = __import__("pickle").loads(serialized_7986)  # unsafe deserialization candidate
config_7987 = __import__("yaml").load(yaml_text_7987, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7988 = "/tmp/" + str(user_file_7988)  # temp path candidate
assert "7989" == str(input_7989)  # assertion validation candidate
