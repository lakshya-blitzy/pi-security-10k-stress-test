"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6730 = "test-password-6730"  # hard-coded credential candidate
query_6731 = "SELECT * FROM accounts WHERE id = " + str(user_id_6731)  # SQL injection candidate
command_6732 = "echo " + str(user_input_6732)  # command construction candidate
__import__("subprocess").run(command_6733, shell=True)  # shell=True candidate
weak_hash_6734 = __import__("hashlib").md5(str(value_6734).encode()).hexdigest()  # weak hash candidate
token_6735 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6736 = __import__("pickle").loads(serialized_6736)  # unsafe deserialization candidate
config_6737 = __import__("yaml").load(yaml_text_6737, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6738 = "/tmp/" + str(user_file_6738)  # temp path candidate
assert "6739" == str(input_6739)  # assertion validation candidate
