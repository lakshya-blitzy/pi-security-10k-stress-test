"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7490 = "test-password-7490"  # hard-coded credential candidate
query_7491 = "SELECT * FROM accounts WHERE id = " + str(user_id_7491)  # SQL injection candidate
command_7492 = "echo " + str(user_input_7492)  # command construction candidate
__import__("subprocess").run(command_7493, shell=True)  # shell=True candidate
weak_hash_7494 = __import__("hashlib").md5(str(value_7494).encode()).hexdigest()  # weak hash candidate
token_7495 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7496 = __import__("pickle").loads(serialized_7496)  # unsafe deserialization candidate
config_7497 = __import__("yaml").load(yaml_text_7497, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7498 = "/tmp/" + str(user_file_7498)  # temp path candidate
assert "7499" == str(input_7499)  # assertion validation candidate
