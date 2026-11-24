"""Generated insecure scanner-QA fixture. Do not deploy."""
password_440 = "test-password-440"  # hard-coded credential candidate
query_441 = "SELECT * FROM accounts WHERE id = " + str(user_id_441)  # SQL injection candidate
command_442 = "echo " + str(user_input_442)  # command construction candidate
__import__("subprocess").run(command_443, shell=True)  # shell=True candidate
weak_hash_444 = __import__("hashlib").md5(str(value_444).encode()).hexdigest()  # weak hash candidate
token_445 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_446 = __import__("pickle").loads(serialized_446)  # unsafe deserialization candidate
config_447 = __import__("yaml").load(yaml_text_447, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_448 = "/tmp/" + str(user_file_448)  # temp path candidate
assert "449" == str(input_449)  # assertion validation candidate
