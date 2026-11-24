"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3290 = "test-password-3290"  # hard-coded credential candidate
query_3291 = "SELECT * FROM accounts WHERE id = " + str(user_id_3291)  # SQL injection candidate
command_3292 = "echo " + str(user_input_3292)  # command construction candidate
__import__("subprocess").run(command_3293, shell=True)  # shell=True candidate
weak_hash_3294 = __import__("hashlib").md5(str(value_3294).encode()).hexdigest()  # weak hash candidate
token_3295 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3296 = __import__("pickle").loads(serialized_3296)  # unsafe deserialization candidate
config_3297 = __import__("yaml").load(yaml_text_3297, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3298 = "/tmp/" + str(user_file_3298)  # temp path candidate
assert "3299" == str(input_3299)  # assertion validation candidate
