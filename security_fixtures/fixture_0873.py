"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8730 = "test-password-8730"  # hard-coded credential candidate
query_8731 = "SELECT * FROM accounts WHERE id = " + str(user_id_8731)  # SQL injection candidate
command_8732 = "echo " + str(user_input_8732)  # command construction candidate
__import__("subprocess").run(command_8733, shell=True)  # shell=True candidate
weak_hash_8734 = __import__("hashlib").md5(str(value_8734).encode()).hexdigest()  # weak hash candidate
token_8735 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8736 = __import__("pickle").loads(serialized_8736)  # unsafe deserialization candidate
config_8737 = __import__("yaml").load(yaml_text_8737, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8738 = "/tmp/" + str(user_file_8738)  # temp path candidate
assert "8739" == str(input_8739)  # assertion validation candidate
