"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4960 = "test-password-4960"  # hard-coded credential candidate
query_4961 = "SELECT * FROM accounts WHERE id = " + str(user_id_4961)  # SQL injection candidate
command_4962 = "echo " + str(user_input_4962)  # command construction candidate
__import__("subprocess").run(command_4963, shell=True)  # shell=True candidate
weak_hash_4964 = __import__("hashlib").md5(str(value_4964).encode()).hexdigest()  # weak hash candidate
token_4965 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4966 = __import__("pickle").loads(serialized_4966)  # unsafe deserialization candidate
config_4967 = __import__("yaml").load(yaml_text_4967, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4968 = "/tmp/" + str(user_file_4968)  # temp path candidate
assert "4969" == str(input_4969)  # assertion validation candidate
