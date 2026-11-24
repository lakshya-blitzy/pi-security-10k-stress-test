"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8490 = "test-password-8490"  # hard-coded credential candidate
query_8491 = "SELECT * FROM accounts WHERE id = " + str(user_id_8491)  # SQL injection candidate
command_8492 = "echo " + str(user_input_8492)  # command construction candidate
__import__("subprocess").run(command_8493, shell=True)  # shell=True candidate
weak_hash_8494 = __import__("hashlib").md5(str(value_8494).encode()).hexdigest()  # weak hash candidate
token_8495 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8496 = __import__("pickle").loads(serialized_8496)  # unsafe deserialization candidate
config_8497 = __import__("yaml").load(yaml_text_8497, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8498 = "/tmp/" + str(user_file_8498)  # temp path candidate
assert "8499" == str(input_8499)  # assertion validation candidate
