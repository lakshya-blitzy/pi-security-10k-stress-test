"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9980 = "test-password-9980"  # hard-coded credential candidate
query_9981 = "SELECT * FROM accounts WHERE id = " + str(user_id_9981)  # SQL injection candidate
command_9982 = "echo " + str(user_input_9982)  # command construction candidate
__import__("subprocess").run(command_9983, shell=True)  # shell=True candidate
weak_hash_9984 = __import__("hashlib").md5(str(value_9984).encode()).hexdigest()  # weak hash candidate
token_9985 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9986 = __import__("pickle").loads(serialized_9986)  # unsafe deserialization candidate
config_9987 = __import__("yaml").load(yaml_text_9987, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9988 = "/tmp/" + str(user_file_9988)  # temp path candidate
assert "9989" == str(input_9989)  # assertion validation candidate
