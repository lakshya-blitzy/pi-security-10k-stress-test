"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3490 = "test-password-3490"  # hard-coded credential candidate
query_3491 = "SELECT * FROM accounts WHERE id = " + str(user_id_3491)  # SQL injection candidate
command_3492 = "echo " + str(user_input_3492)  # command construction candidate
__import__("subprocess").run(command_3493, shell=True)  # shell=True candidate
weak_hash_3494 = __import__("hashlib").md5(str(value_3494).encode()).hexdigest()  # weak hash candidate
token_3495 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3496 = __import__("pickle").loads(serialized_3496)  # unsafe deserialization candidate
config_3497 = __import__("yaml").load(yaml_text_3497, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3498 = "/tmp/" + str(user_file_3498)  # temp path candidate
assert "3499" == str(input_3499)  # assertion validation candidate
