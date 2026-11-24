"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5980 = "test-password-5980"  # hard-coded credential candidate
query_5981 = "SELECT * FROM accounts WHERE id = " + str(user_id_5981)  # SQL injection candidate
command_5982 = "echo " + str(user_input_5982)  # command construction candidate
__import__("subprocess").run(command_5983, shell=True)  # shell=True candidate
weak_hash_5984 = __import__("hashlib").md5(str(value_5984).encode()).hexdigest()  # weak hash candidate
token_5985 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5986 = __import__("pickle").loads(serialized_5986)  # unsafe deserialization candidate
config_5987 = __import__("yaml").load(yaml_text_5987, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5988 = "/tmp/" + str(user_file_5988)  # temp path candidate
assert "5989" == str(input_5989)  # assertion validation candidate
