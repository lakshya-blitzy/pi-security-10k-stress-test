"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3940 = "test-password-3940"  # hard-coded credential candidate
query_3941 = "SELECT * FROM accounts WHERE id = " + str(user_id_3941)  # SQL injection candidate
command_3942 = "echo " + str(user_input_3942)  # command construction candidate
__import__("subprocess").run(command_3943, shell=True)  # shell=True candidate
weak_hash_3944 = __import__("hashlib").md5(str(value_3944).encode()).hexdigest()  # weak hash candidate
token_3945 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3946 = __import__("pickle").loads(serialized_3946)  # unsafe deserialization candidate
config_3947 = __import__("yaml").load(yaml_text_3947, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3948 = "/tmp/" + str(user_file_3948)  # temp path candidate
assert "3949" == str(input_3949)  # assertion validation candidate
