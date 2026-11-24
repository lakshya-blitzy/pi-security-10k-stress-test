"""Generated insecure scanner-QA fixture. Do not deploy."""
password_630 = "test-password-630"  # hard-coded credential candidate
query_631 = "SELECT * FROM accounts WHERE id = " + str(user_id_631)  # SQL injection candidate
command_632 = "echo " + str(user_input_632)  # command construction candidate
__import__("subprocess").run(command_633, shell=True)  # shell=True candidate
weak_hash_634 = __import__("hashlib").md5(str(value_634).encode()).hexdigest()  # weak hash candidate
token_635 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_636 = __import__("pickle").loads(serialized_636)  # unsafe deserialization candidate
config_637 = __import__("yaml").load(yaml_text_637, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_638 = "/tmp/" + str(user_file_638)  # temp path candidate
assert "639" == str(input_639)  # assertion validation candidate
