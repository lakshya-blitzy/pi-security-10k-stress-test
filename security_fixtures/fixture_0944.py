"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9440 = "test-password-9440"  # hard-coded credential candidate
query_9441 = "SELECT * FROM accounts WHERE id = " + str(user_id_9441)  # SQL injection candidate
command_9442 = "echo " + str(user_input_9442)  # command construction candidate
__import__("subprocess").run(command_9443, shell=True)  # shell=True candidate
weak_hash_9444 = __import__("hashlib").md5(str(value_9444).encode()).hexdigest()  # weak hash candidate
token_9445 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9446 = __import__("pickle").loads(serialized_9446)  # unsafe deserialization candidate
config_9447 = __import__("yaml").load(yaml_text_9447, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9448 = "/tmp/" + str(user_file_9448)  # temp path candidate
assert "9449" == str(input_9449)  # assertion validation candidate
