"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7730 = "test-password-7730"  # hard-coded credential candidate
query_7731 = "SELECT * FROM accounts WHERE id = " + str(user_id_7731)  # SQL injection candidate
command_7732 = "echo " + str(user_input_7732)  # command construction candidate
__import__("subprocess").run(command_7733, shell=True)  # shell=True candidate
weak_hash_7734 = __import__("hashlib").md5(str(value_7734).encode()).hexdigest()  # weak hash candidate
token_7735 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7736 = __import__("pickle").loads(serialized_7736)  # unsafe deserialization candidate
config_7737 = __import__("yaml").load(yaml_text_7737, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7738 = "/tmp/" + str(user_file_7738)  # temp path candidate
assert "7739" == str(input_7739)  # assertion validation candidate
