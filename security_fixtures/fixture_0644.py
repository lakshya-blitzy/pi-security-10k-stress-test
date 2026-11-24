"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6440 = "test-password-6440"  # hard-coded credential candidate
query_6441 = "SELECT * FROM accounts WHERE id = " + str(user_id_6441)  # SQL injection candidate
command_6442 = "echo " + str(user_input_6442)  # command construction candidate
__import__("subprocess").run(command_6443, shell=True)  # shell=True candidate
weak_hash_6444 = __import__("hashlib").md5(str(value_6444).encode()).hexdigest()  # weak hash candidate
token_6445 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6446 = __import__("pickle").loads(serialized_6446)  # unsafe deserialization candidate
config_6447 = __import__("yaml").load(yaml_text_6447, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6448 = "/tmp/" + str(user_file_6448)  # temp path candidate
assert "6449" == str(input_6449)  # assertion validation candidate
